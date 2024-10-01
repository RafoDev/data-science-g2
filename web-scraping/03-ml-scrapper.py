import requests
from bs4 import BeautifulSoup

def page_to_file(url, filename):
  response = requests.get(url)
  if response.status_code == 200:
    with open(filename+".html", "wb") as file:
      file.write(response.content)
  else:
    print("error: ", response.status_code)

#page_to_file(url, "mercado-libre")

def get_file_content(filename):
  with open(filename, "r", encoding="utf-8") as file:
    return file.read()

def get_products(query):
  url = f"https://listado.mercadolibre.com.pe/{query}"
  # response = requests.get(url)
  # html_doc = response.text

  html_doc = get_file_content("mercado-libre.html")

  html = BeautifulSoup(html_doc, "html.parser")

  product_list = html.find_all("li", {"class":"ui-search-layout__item shops__layout-item"})

  for product in product_list:
    # titulo, precio, descuento, calificacion, reviews, variaciones, info delivery, best seller
    element_title = product.h2
    product_title = element_title.get_text()
    
    print(product_title)

get_products("teclado")
# soup = BeautifulSoup(html_doc)
# print(soup.prettify())
