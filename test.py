html_doc = """<h1>Hé ho! </h1>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"lxml")
print(soup.get_text())
