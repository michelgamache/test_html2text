html_doc = """<h1>Hé ho! </h1>"""

## commentaire 1

from bs4 import BeautifulSoup

## commentaire 2
soup = BeautifulSoup(html_doc,"lxml")
print(soup.get_text())
