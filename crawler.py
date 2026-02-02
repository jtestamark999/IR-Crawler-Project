from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen
from urllib.parse import urljoin

url="https://nlp.stanford.edu/IR-book/information-retrieval-book.html"
non_visited=[url]
visited=set()

#check the url
def is_url_ok(url):
    if not url.startswith("http"):
        return False
    if not url.endswith(".html"):
        return False
    if "nlp.stanford.edu" not in url:
        return False
    return True

while non_visited:
    current_url = non_visited.pop(0)
    if current_url in visited:
        continue
    print("Visiting", current_url)

    visited.add(current_url)
    try:
        page = urlopen(current_url)
    except:
        continue
    if page.getcode() != 200:
        continue

    text = ""
    html = page.read().decode("utf-8")
    soup = bs(html, 'html.parser')

    title_tag = soup.find("h1")

    if not title_tag:
        title_tag = soup.find("h2")
    if title_tag:
        title = title_tag.get_text()
    else:
        title = "No title"

    for p in soup.find_all("p"):
         text += p.get_text() + "\n"

    filename = f"page_{len(visited)}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(current_url+"\n")
        f.write(title+"\n\n")
        f.write(text)

    for link in soup.find_all("a"):

        href = link.get("href")

        if not href:
            continue

        full_url=urljoin(current_url, href)

        if is_url_ok(full_url):
            if full_url not in visited:
                non_visited.append(full_url)

    time.sleep(1)





