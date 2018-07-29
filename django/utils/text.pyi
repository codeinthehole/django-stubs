from django.utils.safestring import SafeText
from typing import (
    Iterator,
    List,
    Optional,
    Union,
)


def _format_lazy(format_string: str, *args, **kwargs) -> str: ...


def camel_case_to_spaces(value: str) -> str: ...


def capfirst(x: Optional[str]) -> Optional[str]: ...


def compress_sequence(sequence: Union[List[bytes], map]) -> Iterator[bytes]: ...


def compress_string(s: bytes) -> bytes: ...


def get_text_list(list_: List[str], last_word: str = ...) -> str: ...


def get_valid_filename(s: str) -> str: ...


def normalize_newlines(text: str) -> str: ...


def phone2numeric(phone: str) -> str: ...


def slugify(value: str, allow_unicode: bool = ...) -> SafeText: ...


def smart_split(text: str) -> Iterator[str]: ...


def unescape_entities(text: str) -> str: ...


def unescape_string_literal(s: str) -> str: ...


def wrap(text: str, width: int) -> str: ...


class StreamingBuffer:
    def __init__(self) -> None: ...
    def read(self) -> bytes: ...
    def write(self, val: bytes) -> None: ...


class Truncator:
    def __init__(self, text: str) -> None: ...
    def _text_chars(self, length: int, truncate: Optional[str], text: str, truncate_len: int) -> str: ...
    def _text_words(self, length: int, truncate: Optional[str]) -> str: ...
    def _truncate_html(self, length: int, truncate: Optional[str], text: str, truncate_len: int, words: bool) -> str: ...
    def add_truncation_text(self, text: str, truncate: Optional[str] = ...) -> str: ...
    def chars(self, num: int, truncate: Optional[str] = ..., html: bool = ...) -> str: ...
    def words(self, num: int, truncate: Optional[str] = ..., html: bool = ...) -> str: ...