from urllib.parse import urlparse


def is_internal(url: str, base: str) -> bool:
    return urlparse(url).netloc == urlparse(base).netloc
