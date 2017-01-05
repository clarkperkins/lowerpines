import json
from json import JSONEncoder
from typing import List, Dict, Any

from lowerpines.endpoints import Request
from lowerpines.gmi import GMI


class Block:
    user_id = ... #  type: str
    blocked_user_id = ... #  type: str
    created_at = ... #  type: str
    gmi = ... #  type: GMI

    def __init__(self, gmi: GMI) -> None: ...
    def get_all(self, user_id: str) -> List['Block']: ...
    @staticmethod
    def block_exists(gmi: GMI, user_id: str, other_user_id: str) -> 'Block': ...
    @staticmethod
    def block(gmi: GMI, user_id: str, other_user_id: str) -> 'Block': ...
    @staticmethod
    def unblock(gmi: GMI, user_id: str, other_user_id: str) -> None: ...
    @classmethod
    def from_json(cls, gmi: GMI, json: Any) -> 'Block': ...


class BlockIndexRequest(Request):
    user_id = ... #  type: str

    def __init__(self, gmi: GMI, user_id: str) -> None: ...
    def mode(self) -> str: ...
    def parse(self, response: dict) -> List[Block]: ...
    def args(self) -> Dict[str, Any]: ...
    def url(self) -> str: ...


class BlockBetweenRequest(Request):
    user_id = ... #  type: str
    other_user_id = ... #  type: str

    def __init__(self, gmi: GMI, user_id: str, other_user_id: str) -> None: ...
    def mode(self) -> str: ...
    def parse(self, response: dict) -> Any: ...
    def args(self) -> dict: ...
    def url(self) -> str: ...


class BlockCreateRequest(Request):
    user_id = ... # type: str
    other_user_id = ... # type: str

    def __init__(self, gmi: GMI, user_id: str, other_user_id: str) -> None: ...
    def mode(self) -> str: ...
    def parse(self, response: dict) -> None: ...
    def args(self) -> dict: ...
    def url(self) -> str: ...


class BlockUnblockRequest(Request):
    user_id = ... # type: str
    other_user_id = ... # type: str

    def __init__(self, gmi: GMI, user_id: str, other_user_id: str) -> None: ...
    def mode(self) -> str: ...
    def parse(self, response: dict) -> None: ...
    def args(self) -> dict: ...
    def url(self) -> str: ...
