from typing import Optional
import pydantic


class Status(pydantic.BaseModel):
    affects: Optional[str] = pydantic.Field(..., description='Packagenames, see \'affects\'-field in control-BTS manual')
    archived: int = pydantic.Field(..., description='The bug is archived or not')
    blockedby: Optional[str] = pydantic.Field(..., description='Bugreports this bug is blocked by')
    blocks: Optional[str] = pydantic.Field(..., description='Bugreports this bug blocks')
    bug_num: int = pydantic.Field(..., description='The bugnumber')
    date: int = pydantic.Field(..., description='Date of bug creation')
    done: str = pydantic.Field(..., description='Maintainer who closed the bug, or empty string if it\'s not closed')
    fixed_versions: Optional[list[str]] = pydantic.Field(..., description='Version Numbers, can be empty even if the bug is fixed')
    forwarded: Optional[str] = pydantic.Field(..., description='some URL, sometimes an email address')
    found_versions: Optional[list[str]] = pydantic.Field(..., description='Version Numbers')
    last_modified: int = pydantic.Field(..., description='Date of last update')
    location: str = pydantic.Field(..., description='Always \'db-h\' or \'archive\'')
    mergedwith: Optional[str] = pydantic.Field(..., description='The bugs this bug was merged with')
    msgid: str = pydantic.Field(..., description='Message ID of the bugreport')
    originator: str = pydantic.Field(..., description='Submitter of the bugreport')
    owner: Optional[str] = pydantic.Field(..., description='default: empty, otherwise: who is responsible for fixing')
    package: str = pydantic.Field(..., description='Package of the Bugreport')
    pending: str = pydantic.Field(..., description='Either \'pending\' or \'done\'')
    severity: str = pydantic.Field(..., description='Severity of the bugreport')
    source: str = pydantic.Field(..., description='Source package of the Bugreport')
    subject: str = pydantic.Field(..., description='Subject/Title of the bugreport')
    summary: Optional[str] = pydantic.Field(..., description='Arbitrary text')
    tags: Optional[list[str]] = pydantic.Field(..., description='Tags of the bugreport')
    unarchived: Optional[str] = pydantic.Field(..., description='Has the bug been unarchived and can be archived again')
    rest_attrs: str = pydantic.Field(..., description='unknown attrs')

    # Don't use the ones below
    log_modified: int
    keywords: Optional[str]
    fixed_date: Optional[list[int]]
    found_date: Optional[list[str]]
    id: int
    found: Optional[str]  # dict[str, bool]
    fixed: Optional[int]
