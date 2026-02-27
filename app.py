import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

VIDEO_EXTENSIONS = ('.mp4', '.webm', '.ogg')

VIDEO_EMBED_HOST_PATTERNS = (
    'youtube.com/embed/',
    'youtube-nocookie.com/embed/',
    'youtu.be/',
    'player.vimeo.com/video/', 
)

def is_internal(url: str, base: str) -> bool:
    return urlparse(url).netloc == urlparse(base).netloc

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

    for tag in soup.find_all('source', src=True):
        if _src_looks_like_video(tag.get('src')):
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

def crawl_site(start_url: str, max_links: int = 40, timeout: int = 10, user_agent: str = None):
    visited = set()
    pages_with_videos = []

    headers = {}
    if user_agent:
        headers["User-Agent"] = user_agent
    else:
        headers["User-Agent"] = "Mozilla/5.0 (compatible; VideoCrawler/1.0; +https://example.com/bot)"

    def crawl(url: str):
        if len(visited) >= max_links:
            return
        if url in visited:
            return

        visited.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            if has_video(soup):
                pages_with_videos.append(url)

            for link in soup.find_all('a', href=True):
                href = urljoin(url, link.get('href'))
                href = href.split('#', 1)[0]

                if is_internal(href, start_url) and href not in visited:
                    crawl(href)

        except requests.exceptions.RequestException as e:
            print(f"Failed to crawl {url}: {e}")

    crawl(start_url)
    return pages_with_videos

def save_links_as_txt(links, filename: str = 'links.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

if __name__ == "__main__":
    pages_with_videos = crawl_site("'https://www.example.com/'", max_links=40)
    save_links_as_txt(pages_with_videos, filename='links.txt')
    print(f"Found {len(pages_with_videos)} pages with videos. Saved to links.txt")