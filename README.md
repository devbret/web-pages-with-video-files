# Web Pages With Video Files

Targeted web scraper which discovers and lists all pages containing embedded or hosted videos on a specified website, saving results in a structured text file.

## Application Overview

Leverages libraries like `requests`, `BeautifulSoup` and Python’s built-in modules to analyze web page structures. It checks for video content in multiple ways; such as direct `<video>` tags with supported extensions, `<source>` or generic tags pointing to video files and embedded players via `<iframe>` elements. The crawler respects the `max_links` limit to avoid excessive requests and includes error handling.

Once the application identifies pages with videos, the script compiles a list of these URLs and saves them to a text file. The modular design allows customization, while maintaining efficiency through crawling. Overall, the tool automates the tedious process of manually searching for pages with videos on a website.

## Basic Setup Instructions

Below are instructions for installing and running this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/web-pages-with-video-files.git`

4. Navigate to the repo's directory: `cd web-pages-with-video-files`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Edit the `app.py` file (line 101) to include the target URL and max number of links

9. Run the script: `python3 app.py`

10. Exit the virtual environment: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Crawl websites to identify and list all pages containing embedded or hosted videos

- Follow internal links while enforcing a configurable limit to avoid overloading servers or getting blocked

- Detect videos across formats and platforms by parsing HTML tags

- Generate a structured text file of all URLs containing videos

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
