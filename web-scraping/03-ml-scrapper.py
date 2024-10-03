import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from mysql import connector

load_dotenv()

config = {
  "host":"localhost",
  "user":"root",
  "password": os.getenv("DB_PASSWORD"),
  "database": "db_codigo"
}

url = f"https://listado.mercadolibre.com.pe/teclados"

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
  response = requests.get(url)
  html_doc = response.text

  #html_doc = get_file_content("mercado-libre.html")

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

    # best seller
    highlight_info = product.find(class_="poly-component__highlight")
    # product_best_seller = False

    # if highlight_info and highlight_info.string == "MÁS VENDIDO":
    #     product_best_seller = True
    
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

def save_products(products):
	with connector.connect(**config) as db:
		with db.cursor() as cursor:
			try: 
				cursor.execute("""
					create table product(
						id int primary key auto_increment,
						title varchar(200) unique,
						price float,
            discount int,
						free_shipping bool,
						rating float,
						reviews int,
						variations int,
						best_seller bool
					)
				""")
				db.commit()
			except Exception as error:
				print("error: ", error)

			query_insert = """
				insert into product(title, price, discount, free_shipping, rating, reviews, variations, best_seller)
				values (%s,%s,%s,%s,%s,%s,%s,%s)
			"""
			try:
				cursor.executemany(query_insert, products)
				db.commit()
			except Exception as error:
				print("error: ", error)

query = "razer"
products = get_products(query)
save_products(products)

			
