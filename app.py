from modules.crawler import crawl_site
from modules.output import save_links_as_txt


if __name__ == "__main__":
    pages_with_videos = crawl_site("https://www.example.com/", max_pages=40)
    save_links_as_txt(pages_with_videos, filename='links.txt')
    print(f"Found {len(pages_with_videos)} pages with videos. Saved to links.txt")
