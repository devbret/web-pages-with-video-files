import requests
from collections import deque
from urllib.parse import urljoin
from bs4 import BeautifulSoup

from .config import DEFAULT_USER_AGENT
from .detection import has_video
from .urls import is_internal


def crawl_site(start_url: str, max_pages: int = 40, timeout: int = 10, user_agent: str = None):
    pages_with_videos = []
    pages_crawled = 0

    headers = {}
    if user_agent:
        headers["User-Agent"] = user_agent
    else:
        headers["User-Agent"] = DEFAULT_USER_AGENT

    seen = {start_url}
    queue = deque([start_url])

    while queue and pages_crawled < max_pages:
        url = queue.popleft()
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to crawl {url}: {e}")
            continue

        pages_crawled += 1

        soup = BeautifulSoup(response.text, 'html.parser')

        if has_video(soup):
            pages_with_videos.append(url)

        for link in soup.find_all('a', href=True):
            href = urljoin(url, link.get('href'))
            href = href.split('#', 1)[0]

            if is_internal(href, start_url) and href not in seen:
                seen.add(href)
                queue.append(href)

    return pages_with_videos
