import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

def is_internal(url, base):
    return urlparse(url).netloc == urlparse(base).netloc

def has_video(soup):
    return soup.find('video') is not None or any(tag['src'].endswith(('.mp4', '.webm', '.ogg')) for tag in soup.find_all('source', src=True))

def crawl_site(start_url, max_links=100):
    visited = set()
    pages_with_videos = []

    def crawl(url):
        if len(visited) >= max_links:
            return
        if url in visited:
            return
        visited.add(url)
        print(f"Crawling: {url}")

        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            if has_video(soup):
                pages_with_videos.append(url)

            for link in soup.find_all('a', href=True):
                href = urljoin(url, link.get('href'))
                if is_internal(href, start_url) and href not in visited:
                    crawl(href)

        except requests.exceptions.RequestException as e:
            print(f"Failed to crawl {url}: {e}")

    crawl(start_url)
    return pages_with_videos

def save_links_as_txt(links, filename='links.txt'):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')

pages_with_videos = crawl_site('https://www.example.com/')
save_links_as_txt(pages_with_videos)
