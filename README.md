# Discover Web Pages With Video Files

Crawl a specific number of web pages on an individual domain for videos. If found, a .txt file is created containing all related internal links.

## Set Up

### Programs Needed 

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) (When installing on Windows, make sure you check the ["Add python 3.xx to PATH"](https://hosting.photobucket.com/images/i/bernhoftbret/python.png) box.)

### Steps

1. Install the above programs.
2. Open a shell window (For Windows open PowerShell, for MacOS open Terminal & for Linux open your distro's terminal emulator).
3. Clone this repository using `git` by running the following command; `git clone https://github.com/devbret/web-pages-with-video-files`.
4. Navigate to the repo's directory by running; `cd web-pages-with-video-files`.
5. Install the needed dependencies for running the script by running; `pip install -r requirements.txt`.
6. Edit the app.py file on line 46, to include the website that you would like to visualize. Also consider changing the maximum number of links to crawl on line 11.
8. Run the script with the command `python3 app.py`.
9. When finished, view the generated .txt file for the internal URLs of web pages containing a video file.
