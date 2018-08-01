# Stubs for django.contrib.sessions.backends.db (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.contrib.sessions.backends.base import SessionBase
from typing import Any, Optional

from datetime import datetime
from django.contrib.sessions.base_session import AbstractBaseSession
from django.contrib.sessions.models import Session
from typing import Dict, Optional, Type, Union

class SessionStore(SessionBase):
    def __init__(self, session_key: Optional[str] = ...) -> None: ...
    @classmethod
    def get_model_class(cls) -> Type[Session]: ...
    def model(self) -> Type[AbstractBaseSession]: ...
    _session_key: Any = ...
    def _get_session_from_db(self) -> Optional[AbstractBaseSession]: ...
    def load(self) -> Dict[str, Union[str, int]]: ...
    def exists(self, session_key: Optional[str]) -> bool: ...
    modified: bool = ...
    def create(self) -> None: ...
    def create_model_instance(
        self, data: Dict[str, Union[str, int, datetime]]
    ) -> AbstractBaseSession: ...
    def save(self, must_create: bool = ...) -> None: ...
    def delete(self, session_key: Optional[str] = ...) -> None: ...
    @classmethod
    def clear_expired(cls) -> None: ...