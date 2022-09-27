from typing import Optional
import pydantic


class Status(pydantic.BaseModel):
    affects: Optional[str]
    archived: int
    blockedby: Optional[str]
    blocks: Optional[str]
    bug_num: int
    date: int
    done: str
    fixed: Optional[int]
    fixed_date: Optional[list[int]]
    fixed_versions: Optional[list[str]]
    forwarded: Optional[str]
    found_date: Optional[list[str]]
    found_versions: Optional[list[str]]
    # found: list[str]  # dict[str, bool]
    id: int
    keywords: Optional[str]
    last_modified: int
    location: str
    log_modified: int
    mergedwith: Optional[str]
    msgid: str
    originator: str
    owner: Optional[str]
    package: str
    pending: str
    severity: str
    source: str
    subject: str
    summary: Optional[str]
    tags: Optional[str]
    unarchived: Optional[str]
    rest_attrs: str
