import requests
from bs4 import BeautifulSoup
from prefect import task

@task(name="Extraer productos de Mercado Libre")
def task_extract_products(query):
  # URL DE LA PRIMERA PÁGINA DE BÚSQUEDA DE 'QUERY'
  url = f"https://listado.mercadolibre.com.pe/{query}"
  response = requests.get(url)
  html_doc = response.text

  html = BeautifulSoup(html_doc, "html.parser")

  product_list = html.find_all("li", {"class":"ui-search-layout__item shops__layout-item"})

  products = []

  for product in product_list:
    element_title = product.h2
    
    product_title = element_title.get_text()
    product_price = float(product.find(class_="andes-money-amount andes-money-amount--cents-superscript").get_text()[2:].replace(',', '.'))
    shipping_info = product.find(class_="poly-component__shipping")
    product_free_shipping = True if shipping_info and shipping_info.get_text().find("gratis") else False

    discount_info = product.find(class_="andes-money-amount__discount")
    product_discount = discount_info.string if discount_info else "0"
    product_discount = int(product_discount.replace("% OFF",""))

    rating_info = product.find(class_="poly-reviews__rating")
    product_rating = float(rating_info.string) if rating_info else 0
      
    reviews_info = product.find(class_="poly-reviews__total")
    product_reviews = int(reviews_info.string[1: -1]) if reviews_info else 0

    variations_info = product.find(class_="poly-component__variations-text")
    product_variations = int(variations_info.string.split()[2]) if variations_info else 0
    highlight_info = product.find(class_="poly-component__highlight")
    
    product_best_seller = True if highlight_info and highlight_info.string == "MÁS VENDIDO" else False

    products.append((
      product_title,
      product_price,
      product_discount,
      product_free_shipping,
      product_rating,
      product_reviews,
      product_variations,
      product_best_seller
    ))

  return products