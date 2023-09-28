import sqlite3
from bs4 import BeautifulSoup
import requests

# 1
url = "https://www.google.com/"
response = requests.get(url)
html = response.text
# 2
conn = sqlite3.connect("links.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS links (url TEXT)")

# 3
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all("a"):
    url = link.get("href")
    if url:
        c.execute("INSERT INTO links VALUES (?)", (url,))

conn.commit()
conn.close()
