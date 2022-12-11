from __future__ import annotations

import string


class AsciiArt:
    name: str
    match: str
    color: str
    ascii: str

    def __init__(self, match: str, color: str, ascii: str, name: str | None = None):
        self.match = match
        self.color = color
        self.ascii = ascii
        self.name = name or self.get_friendly_name()

    def get_friendly_name(self) -> str:
        return self.match.split("|")[0].strip(string.punctuation + '* ') \
            .replace('"', '').replace('*', '')
