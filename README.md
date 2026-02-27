# Discover Web Pages With Video Files

A lightweight recursive web crawler which starts from a given URL, traverses internal links up to a specified limit and identifies pages containing embedded video content.

## Overview

This application analyzes each page’s HTML using BeautifulSoup to detect native `<video>` elements, direct video file sources and embedded video players such as YouTube iframes, including common variants. When a page containing video content is found, its URL is recorded and after the crawl completes, all matching pages are saved to a text file for later review or analysis.

## Set Up Instructions

Below are instructions for installing and running this application.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository using `git` by running the following command: `git clone git@github.com:devbret/web-pages-with-video-files.git`

4. Navigate to the repo's directory by running: `cd web-pages-with-video-files`

5. Install the needed dependencies for the script by running: `pip install -r requirements.txt`

6. Edit the `app.py` file on line 101, to include the website that you would like to visualize; also consider changing the maximum number of links to crawl on line 54

7. Run the script with the command `python3 app.py`

8. When finished, view the generated `.txt` file for the internal URLs of web pages containing a video file
