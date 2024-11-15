from dataclasses import dataclass, asdict


@dataclass
class CompanyInfo:
    name: str
    founded: int

    def to_dict(self):
        return asdict(self)


@dataclass
class LaunchSite:
    name: str
    full_name: str
    launches: list[str]
    num_launches: int = None

    def __post_init__(self):
        if not self.num_launches:
            self.num_launches = len(self.launches)

    def to_dict(self):
        return asdict(self)
