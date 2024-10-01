from bs4 import BeautifulSoup

# 1. Obtener el documento HTML
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title title2 test"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story1">...</p>
"""

# 2. Parsear el documento a una estructura manejable
soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())

# 3. Buscar data

print(soup.title)
print(soup.p)
print(soup.title.name)
print(soup.title.string)

print(soup.p["class"])

# SON LO MISMO
print(soup.find("a"))
print(soup.a)

print(soup.find_all("a"))

print(soup.find("p", {"class" : "story1"}))
print(soup.find("p", class_ = "story1"))

print(soup.find_all(href = True))