from bs4 import BeautifulSoup

from .config import VIDEO_EXTENSIONS, VIDEO_EMBED_HOST_PATTERNS


def _src_looks_like_video(src: str) -> bool:
    if not src:
        return False
    src = src.strip().lower()
    return src.endswith(VIDEO_EXTENSIONS)


def _src_looks_like_embed(src: str) -> bool:
    if not src:
        return False
    src = src.strip().lower()
    return any(pat in src for pat in VIDEO_EMBED_HOST_PATTERNS)


def has_video(soup: BeautifulSoup) -> bool:
    if soup.find('video') is not None:
        return True

    for tag in soup.find_all(src=True):
        if _src_looks_like_video(tag.get('src')):
            return True

    for iframe in soup.find_all('iframe'):
        candidates = [
            iframe.get('src'),
            iframe.get('data-src'),
            iframe.get('data-lazy-src'),
            iframe.get('data-original'),
        ]
        for src in candidates:
            if _src_looks_like_embed(src):
                return True

    return False
