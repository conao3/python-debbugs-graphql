import json
from typing import Any
import requests
import jinja2
import xml.etree.ElementTree

from . import types


jinja_env = jinja2.Environment()


class Client:
    def __init__(self):
        self.url = "https://debbugs.gnu.org/cgi/soap.cgi"
        self.headers = {
            'content-type': 'text/xml; charset=utf-8',
            'SOAPAction': 'Debbugs/SOAP',
        }

    def get_status(self, bugnumber: int) -> types.Status:
        res = self.get_statuses([bugnumber])
        return res[0]

    def get_statuses(self, bugnumbers: list[int]) -> list[types.Status]:
        tmpl = jinja_env.from_string("""\
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope
    soapenc:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:ns3="urn:Debbugs/SOAP/TYPES"
    xmlns:ns1="urn:Debbugs/SOAP"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
>
<soap:Body>
<ns1:get_status>
<ns1:bugs xsi:type="soapenc:Array" soapenc:arrayType="xsd:int[{{ bugnumbers | length }}]">
{% for bugnumber in bugnumbers %}
<ns1:bugs xsi:type="xsd:int">{{ bugnumber }}</ns1:bugs>
{%- endfor %}
</ns1:bugs>
</ns1:get_status>
</soap:Body>
</soap:Envelope>
""")
        body = tmpl.render(bugnumbers=bugnumbers)
        res = requests.post(self.url, data=body, headers=self.headers)
        if not res.ok:
            raise Exception(res.text)

        root = xml.etree.ElementTree.fromstring(res.text)
        values = root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{urn:Debbugs/SOAP}get_statusResponse/*/{urn:Debbugs/SOAP}item/{urn:Debbugs/SOAP}value')

        prefix_len = len('{urn:Debbugs/SOAP}')
        keys = list(types.Status.__fields__.keys())
        ret: list[types.Status] = []
        for val in values:
            attrs: dict[str, Any] = {}
            rest_attrs = {}
            for attr in val:
                if attr.tag[prefix_len:] in keys:
                    attrs[attr.tag[prefix_len:]] = attr.text
                else:
                    rest_attrs[attr.tag[prefix_len:]] = attr.text

            ret.append(types.Status(**attrs, rest_attrs=json.dumps(rest_attrs)))

        return ret

client = Client()
