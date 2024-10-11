import requests
from bs4 import BeautifulSoup
from prefect import task, flow

query = "kindle"
url = f"https://www.amazon.com/-/es/s?k={query}&crid=1P9AP4I528NAZ&qid=1728607401&sprefix=%2Caps%2C149&ref=sr_pg_1"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}

def page_to_file(url, filename):
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    with open(filename+".html", "wb") as file:
      file.write(response.content)
  else:
    print("error: ", response.status_code)

# page_to_file(url, "amazon")

def get_file_content(filename):
  with open(filename, "r", encoding="utf-8") as file:
    return file.read()

@task(name="Extracción de productos de amazon")
def task_extract_products(url):

  products = []

  # Scraping Real (requests)
  # response = requests.get(url, headers=headers)
  # html_content = response.text

  # Scraping para practicar (sitio estático)
  html_content = get_file_content("amazon.html")
  html = BeautifulSoup(html_content, "html.parser")

  # TODO: FIND_ALL DE LOS PRODUCTOS, RECORRER Y EXTRAER INFORMACIÓN DE CADA UNO
  product_element = html.find("div",{"data-asin":"B09SWTG9GF"})
  product_title = product_element.find("span", class_ = "a-size-medium a-color-base a-text-normal").string
  product = (product_title, )
  products.append(product)

  return products

@task(name="Cargar productos a BD")
def task_load_products():
  pass

@flow(name="Flujo principal")
def main_flow():
  products = task_load_products(url)
  task_load_products(products)