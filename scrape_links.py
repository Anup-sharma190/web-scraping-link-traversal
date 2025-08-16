"""
Project: Web Scraping with BeautifulSoup - Link Traversal Demo
Skills: Python | Web Scraping | BeautifulSoup | SSL Handling

Description:
------------
This project demonstrates how to scrape web pages using Python’s urllib
and BeautifulSoup library. It starts from a given URL, then repeatedly
retrieves and follows a link at a user-defined position for a specified
number of iterations.

Key Features:
- Handles SSL certificate errors safely.
- Uses BeautifulSoup to parse HTML pages.
- Iteratively retrieves links from web pages.
- Prints each retrieved URL step by step.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ---------------- Step 1: Ignore SSL certificate errors ----------------
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ---------------- Step 2: User Inputs ----------------
url = input('Enter URL: ')
count = int(input('Enter count: '))       # how many times to repeat
position = int(input('Enter position: ')) - 1   # which link position to follow

# ---------------- Step 3: Traverse Links ----------------
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    # Get the link at the required position
    url = tags[position].get('href', None)
    print("Retrieving:", url)
