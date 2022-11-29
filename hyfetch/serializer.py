from __future__ import annotations

import dataclasses
import inspect
import json
from datetime import datetime, date


class EnhancedJSONEncoder(json.JSONEncoder):
    """
    An improvement to the json.JSONEncoder class, which supports:
    encoding for dataclasses, encoding for datetime, and sets
    """

    def default(self, o: object) -> object:

        # Support encoding dataclasses
        # https://stackoverflow.com/a/51286749/7346633
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)

        # Support encoding datetime
        if isinstance(o, (datetime, date)):
            return o.isoformat()

        # Support for sets
        # https://stackoverflow.com/a/8230505/7346633
        if isinstance(o, set):
            return list(o)

        return super().default(o)


def json_stringify(obj: object, indent: int | None = None) -> str:
    """
    Serialize json string with support for dataclasses and datetime and sets and with custom
    configuration.
    Preconditions:
        - obj != None
    :param obj: Objects
    :param indent: Indent size or none
    :return: Json strings
    """
    return json.dumps(obj, indent=indent, cls=EnhancedJSONEncoder, ensure_ascii=False)


def from_dict(cls, d: dict):
    return cls(**{k: v for k, v in d.items() if k in inspect.signature(cls).parameters})
