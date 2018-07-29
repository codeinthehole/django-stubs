from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)
from urllib.parse import (
    ParseResult,
    SplitResult,
)


def _is_safe_url(url: str, allowed_hosts: Set[str], require_https: bool = ...) -> bool: ...


def _urlparse(url: str, scheme: str = ..., allow_fragments: bool = ...) -> ParseResult: ...


def _urlsplit(url: str, scheme: str = ..., allow_fragments: bool = ...) -> SplitResult: ...


def base36_to_int(s: str) -> int: ...


def cookie_date(epoch_seconds: float = ...) -> str: ...


def http_date(epoch_seconds: Union[float, int] = ...) -> str: ...


def int_to_base36(i: Union[str, int, Dict[int, int]]) -> str: ...


def is_safe_url(url: Optional[str], allowed_hosts: Optional[Set[str]], require_https: bool = ...) -> bool: ...


def is_same_domain(host: str, pattern: str) -> bool: ...


def limited_parse_qsl(
    qs: str,
    keep_blank_values: bool = ...,
    encoding: str = ...,
    errors: str = ...,
    fields_limit: Optional[int] = ...
) -> List[Tuple[str, str]]: ...


def parse_etags(etag_str: str) -> List[str]: ...


def parse_http_date(date: str) -> int: ...


def parse_http_date_safe(date: str) -> int: ...


def quote_etag(etag_str: str) -> str: ...


def urlencode(query: Any, doseq: bool = ...) -> str: ...


def urlquote(url: str, safe: str = ...) -> str: ...


def urlquote_plus(url: str, safe: str = ...) -> str: ...


def urlsafe_base64_decode(s: Union[str, bytes]) -> bytes: ...


def urlsafe_base64_encode(s: bytes) -> bytes: ...


def urlunquote_plus(quoted_url: str) -> str: ...