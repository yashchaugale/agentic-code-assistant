from dataclasses import dataclass, field


@dataclass
class Repository:

    name: str = ""

    language: str = ""

    framework: str = ""

    entry_point: str = ""

    purpose: str = ""

    important_files: list = field(default_factory=list)

    modules: list = field(default_factory=list)

    relationships: list = field(default_factory=list)

    issues: list = field(default_factory=list)

    suggestions: list = field(default_factory=list)