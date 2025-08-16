# web-scraping-link-traversal
Web Scraping Link Traversal

This project demonstrates web scraping with Python and BeautifulSoup by repeatedly following links from a starting URL. The program retrieves the link at a user-specified position, then continues this process for a given number of iterations.

🔑 Features

Handles SSL certificate errors safely

Parses HTML using BeautifulSoup

Traverses links dynamically based on position and count

Prints each retrieved URL step by step

🚀 How to Run

Clone this repository

git clone https://github.com/your-username/web-scraping-link-traversal.git
cd web-scraping-link-traversal


Run the script

python link_traversal.py


Enter:

A URL (starting point)

The count (how many times to repeat)

The position (which link to follow each time)

📂 Example Run
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 3
Enter position: 2
Retrieving: http://py4e-data.dr-chuck.net/known_by_Quinn.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Charlotte.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Harper.html

🛠️ Skills Demonstrated

Python Web Scraping

BeautifulSoup

HTML Parsing

SSL Handling
