# 1. Obtener el documento HTML (requests)
import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
# 2. Parsear el documento a una estructura manejable (bs4)
  html_doc = response.text
  soup = BeautifulSoup(html_doc, "html.parser")
  # print(soup.prettify())
  # DOS OPCIONES:
  # 1. IR DE CONTENEDOR EN CONTENEDOR HASTA LLEGAR A LOS QUOTES 
  # 2. DIRECTAMENTE BUSCAR LOS QUOTES
  list_of_quotes = soup.find_all("div", {"class":"quote"})

  quotes = []

  # 3. Devolver una lista de quotes.
  # * Cada quote con su: text, autor, tags (texto)
  for quote in list_of_quotes:
    # text = quote.find("span", {"class" : "text"})
    text = quote.span.string
    autor = quote.small.string

    tag_elements = quote.find_all("a", {"class" : "tag"})
    tags = []
    for tag in tag_elements:
      tags.append(tag.string)
    
    quotes.append((text, autor, tags))

  for quote in quotes:
    print(quote)

else:
  print("error: ", response.status_code)



