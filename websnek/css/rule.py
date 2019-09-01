from typing import NamedTuple

class Rule(NamedTuple):
    selectors: list
    declarations: list # of dicts