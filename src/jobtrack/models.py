from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class JobRef:
    source: str
    company: str
    job_id: str


@dataclass
class Posting:
    source: str
    company: str
    job_id: str
    title: str
    url: str
    location: str | None = None
    status: str = "open"
    id: int | None = None
    saved_at: datetime | None = None
    checked_at: datetime | None = None
    closed_at: datetime | None = None

    @property
    def ref(self) -> JobRef:
        return JobRef(self.source, self.company, self.job_id)