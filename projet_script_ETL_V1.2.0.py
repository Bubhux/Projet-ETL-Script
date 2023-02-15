import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import os
from tqdm import tqdm
import csv
import time
import datetime
import statistics
from datetime import datetime


#Bloc des fonctions 
def fonction_main_extract_all_categories(url):
	liste_data_books = []
	liste_categories_urls = []
	liste_categories = []
	liste_categories_final = []

	#Récuperation des titres des catégories
	reponse = requests.get(url)
	page = reponse.content
	if reponse.ok:
		soup = BeautifulSoup(reponse.text, "html.parser")
		categories_titles = soup.find_all("a")

	for categories_titles in soup.find_all("a")[3:53]:
		liste_categories.append(categories_titles.text)
		#print(categories_titles)

	for index, value in enumerate(liste_categories, 1):
		new_categories_titles = (f"{value}")
		text = new_categories_titles
		new_categories_titles = text.replace(" ", "").replace("\n", "")
		liste_categories_final.append(new_categories_titles)
		print(new_categories_titles)

	#Récuperation des urls des catégories 
	soup = BeautifulSoup(reponse.text, "html.parser")
	categories_urls = soup.select("a", class_="nav nav-list")

	for a in categories_urls[3:53]:
		link = (str(a["href"]))
		urls_relative = link.replace("catalogue", "")
		urls_categories = ("http://books.toscrape.com/catalogue" + urls_relative)
		liste_categories_urls.append(urls_categories)
		print(urls_categories)
		
	print("================================================================")

	for base_url in liste_categories_urls:
		liste_data_books.append(loop_exctract_all_pages(base_url))

	return liste_data_books


def loop_exctract_all_pages(url):
	liste_all_urls = [url]
	liste_data_books = []
	loop_all_pages = True
	count_pages = 1
	while loop_all_pages:
		reponse = requests.get(url)
		page = reponse.content
		soup = BeautifulSoup(reponse.text, "html.parser")
		current_elements = soup.select_one("li.current")
		next_page_elements = soup.select_one("li.next > a")
		print (f"Page {count_pages} url catégories {url}")
		count_pages += 1

		if current_elements is True:
			continue

		if current_elements is None:
			print("Aucune next page !")

		#elif current_elements is True:
			#pass

		print("================================================================")

		if next_page_elements:
			next_page_url = next_page_elements.get("href")
			url = urljoin(url, next_page_url)
			print(f"Url next page : {url}")
			liste_all_urls.append(url)

		elif soup.find("ul",class_="next") is None:
			loop_all_pages = False

	for url in liste_all_urls:
		liste_data_books.extend(extract_urls_all_books(url))

	return liste_data_books


def extract_urls_all_books(url):
	liste_data_books = []
	liste_urls_links = []
	title_textes = []
	#count_pages = 1
	reponse = requests.get(url)
	page = reponse.content
	soup = BeautifulSoup(reponse.text, "html.parser")
	current_elements = soup.select_one("li.current")
	next_page_elements = soup.select_one("li.next > a")
	titles = soup.find_all("h3")
	print (f"Url catégories {url}")
	#count_pages += 1

	#if current_elements is None:
		#print("Aucune next page !")

	for title in titles:
		title = title.text
		#title_textes.append(title)
		print(title)

	print("================================================================")

	#Récupération des urls des livres
	reponse = requests.get(url)
	page = reponse.content
	soup = BeautifulSoup(reponse.text, "html.parser")
	urls = soup.find_all("h3")
	#[print(str(h3) + "\n") for h3 in url]
	#print(url)

	for h3 in urls:
		a = h3.find("a", href = True)
		link = a["href"]
		urls_relative = link.replace("../../..", "")
		urls_books = ("http://books.toscrape.com/catalogue" + urls_relative)
		#liste_urls_links.append(urls_books)
		print(urls_books)
		liste_data_books.append(extract_data_books(urls_books))

	return liste_data_books


def extract_data_books(url):
	reponse = requests.get(url)
	page = reponse.content

	print("============================================\n")
	
	#Récupération de product_page_url
	if reponse.ok:
		soup = BeautifulSoup(reponse.text, "html.parser")
		product_page_url_textes = []
		product_page_url = url
		print(f"{product_page_url} : Product page url")
		product_page_url_textes.append(url)
		#for product_page in product_page_url:

		#Récupération de : universal_ product_code (upc)
		soup = BeautifulSoup(reponse.text, "html.parser")
		ths_textes = []
		ths = soup.find_all("th")
		for ths1 in soup.find_all("th")[:1]:
			#[print(str(th.get_text()) + "\n") for th in ths1]
			ths_textes.append(ths1.text)

		#Récupération des valeurs de : universal_ product_code (upc)
		soup = BeautifulSoup(reponse.text, "html.parser")
		tds_textes = []
		tds = soup.find_all("td")
		for tds1 in soup.find_all("td")[:1]:
			#[print(str(td.get_text()) + "\n") for td in tds1]
			tds_textes.append(tds1.text)

			for tds1 in soup.find_all("td")[:1]:
				tds_textes.append(tds1.text)
				text = tds1.text
				characters = "<td></td>"

			for x in range(len(characters)):
				tds1_new_text = text.replace(characters[x],"")

			print(f"Universal product code (upc) : {tds1_new_text}")

		#Récupération de title 
		soup = BeautifulSoup(reponse.text, "html.parser")
		title_textes = []
		titles = soup.find_all("title")
		for title in soup.find_all("title"):
			#print(title.get_text())

			for title in titles:
	  			title_textes.append(title.string)
	  			string_title = (title.string)
	  			characters = "|-\n"

			for x in range(len(characters)):
				string_title = string_title.replace(characters[x],"").replace("Books to Scrape  Sandbox", "")

			print(f"Titre : {string_title}")

		print("============================================\n")

		#Récupération de : price_including_tax
		soup = BeautifulSoup(reponse.text, "html.parser")
		ths_textes = []
		ths = soup.find_all("th")
		for ths2 in soup.find_all("th")[3:4]:
			#[print(str(th.get_text()) + "\n") for th in ths2]
			ths_textes.append(ths2.text)

		#Récupération des valeurs de : price_including_tax
		soup = BeautifulSoup(reponse.text, "html.parser")
		tds_textes = []
		tds = soup.find_all("td")
		for tds2 in soup.find_all("td")[3:4]:
			#[print(str(td.get_text()) + "\n") for td in tds2]
			tds_textes.append(tds2.text)

			for tds2 in soup.find_all("td")[3:4]:
				tds_textes.append(tds2.text)
				text = tds2.text
				characters = "Â"

			for x in range(len(characters)):
				tds2_new_text = text.replace(characters[x],"")

			print(f"Price including tax : {tds2_new_text}")
	

		#Récupération de : price_excluding_tax
		soup = BeautifulSoup(reponse.text, "html.parser")
		ths_textes = []
		ths = soup.find_all("th")

		for ths3 in soup.find_all("th")[2:3]:
			#[print(str(th.get_text()) + "\n") for th in ths3]
			ths_textes.append(ths3.text)

		#Récupération des valeurs de : price_excluding_tax
		soup = BeautifulSoup(reponse.text, "html.parser")
		tds_textes = []
		tds = soup.find_all("td")
		for tds3 in soup.find_all("td")[2:3]:
			#[print(str(td.get_text()) + "\n") for td in tds3]
			tds_textes.append(tds3.text)

			for tds3 in soup.find_all("td")[2:3]:
				tds_textes.append(tds3.text)
				text = tds3.text
				characters = "Â"

			for x in range(len(characters)):
				tds3_new_text = text.replace(characters[x],"")

			print(f"Price excluding tax: {tds3_new_text}")

		print("============================================\n")

		#Récupération de : number_available
		soup = BeautifulSoup(reponse.text, "html.parser")
		ths_textes = []
		ths = soup.find_all("th")
		for ths4 in soup.find_all("th")[5:6]:
			#[print(str(th.get_text()) + "\n") for th in ths4]
			ths_textes.append(ths4.text)

		#Récupération des valeurs de : number_available
		soup = BeautifulSoup(reponse.text, "html.parser")
		tds_textes = []
		tds = soup.find_all("td")
		for tds4 in soup.find_all("td")[5:6]:
			#[print(str(td.get_text()) + "\n") for td in tds4]
			tds_textes.append(tds4.text)

			for tds4 in soup.find_all("td")[5:6]:
				tds_textes.append(tds4.text)
				text = tds4.text
				characters = "<td></td>"

			for x in range(len(characters)):
				tds4_new_text = text.replace(characters[x],"")

			print(tds4_new_text)

		print("============================================\n")

		#Récupération de : product_description
		soup = BeautifulSoup(reponse.text, "html.parser")
		ths_textes = []
		ths = soup.find_all("th")
		for ths5 in soup.find_all("th")[1:2]:
			#[print(str(th.get_text()) + "\n") for th in ths5]
			ths_textes.append(ths5.text)

		#Récupération des valeurs de : product_description
		soup = BeautifulSoup(reponse.text, "html.parser")
		tds_textes = []
		tds = soup.find_all("td")
		for tds5 in soup.find_all("td")[1:2]:
			#[print(str(td.get_text()) + "\n") for td in tds5]
			tds_textes.append(tds5.text)

			for tds5 in soup.find_all("td")[1:2]:
				tds_textes.append(tds5.text)
				text = tds5.text
				characters = "<td></td>"

			for x in range(len(characters)):
				tds5_new_text = text.replace(characters[x],"")

			print(f"Description produit : {tds5_new_text}")
	
		#Récuperation de : category 
		soup = BeautifulSoup(reponse.text, "html.parser")
		cat_textes = []
		categorys = soup.find_all("li")
		for cat in soup.find_all("li")[2:3]:
			#print(cat.get_text())
			#print(cat.text)

			for cat in soup.find_all("li")[2:3]:
	  			#cat_textes.append(cat.text)
	  			text = cat.text
	  			#string_title = (title)
	  			characters = "|-\n"

			for x in range(len(characters)):
				new_text_cat = text.replace(characters[x],"")

			print(f"Catégorie : {new_text_cat}")
		
		print("============================================\n")

		#Récupération de : review_rating
		soup = BeautifulSoup(reponse.text, "html.parser")
		ths_textes = []
		ths = soup.find_all("th")
		for ths6 in soup.find_all("th")[6:7]:
			#[print(str(th.get_text()) + "\n") for th in ths6]
			ths_textes.append(ths6.text)

		#Récupération des valeurs de : review_rating
		soup = BeautifulSoup(reponse.text, "html.parser")
		tds_textes = []
		tds = soup.find_all("td")
		for tds6 in soup.find_all("td")[6:7]:
			#[print(str(td.get_text()) + "\n") for td in tds6]
			tds_textes.append(tds6.text)

			for tds6 in soup.find_all("td")[6:7]:
				tds_textes.append(tds6.text)
				text = tds6.text
				characters = "<td></td>"

			for x in range(len(characters)):
				tds6_new_text = text.replace(characters[x],"")

			print(f"Review rating : {tds6_new_text}")

		#Récupération de image_url
		soup = BeautifulSoup(reponse.text, "html.parser")
		image_url_textes = []
		image_url = soup.select_one("img", class_="item active")
		#print(image_url["src"])
		#image_url_textes.append(image_url)  
		link = image_url["src"]
		#print(link)
		urls = link.replace("../..", "")
		#print(urls)
		url_img = ("http://books.toscrape.com" + urls)
		image_url_textes.append(url_img)
		print(f"Url image : {url_img}") 
		#print(len(urls_books))

		print("============================================\n")

	return ({"category": new_text_cat, "title": string_title, "universal_ product_code (upc)": tds1_new_text, 
			 "price_including_tax": tds2_new_text, "price_excluding_tax": tds3_new_text, "number_available": tds4_new_text,
			 "product_description": tds5_new_text, "review_rating": tds6_new_text, "product_page_url": url, "image_url": url_img})


def write_file_import_csv(data):
	url = "http://books.toscrape.com"
	reponse = requests.get(url)
	page = reponse.content
	liste_categories = []
	liste_categories_final = []
	
	if reponse.ok:
		soup = BeautifulSoup(reponse.text, "html.parser")
		categories_titles = soup.find_all("a")

	for categories_titles in soup.find_all("a")[3:53]:
		liste_categories.append(categories_titles.text)
		#print(categories_title)

	for index, value in enumerate(liste_categories, 1):
		new_categories_titles = (f"{value}")
		text = new_categories_titles
		new_categories_titles = text.replace(" ", "").replace("\n", "")
		liste_categories_final.append(new_categories_titles)
		print(new_categories_titles)  

	count_file = 0
	for i, books_data in zip(liste_categories_final, data):
		with open(f"{i} data.csv", "w", newline="", encoding="utf-8") as file_csv:
			field_names = ["category", "title", "universal_ product_code (upc)", "price_including_tax", "price_excluding_tax", "number_available", 
			               "product_description", "review_rating", "product_page_url", "image_url"]
			
			writer = csv.DictWriter(file_csv, delimiter=";", lineterminator="\n", dialect="excel", fieldnames=field_names)
			writer.writeheader()
			writer.writerows(books_data)
			count_file += 1

	print(f"Total {count_file} fichiers csv écris sur {len(liste_categories_final)}")


def download_all_images(url):
	reponse = requests.get(url)
	page = reponse.content
	try: 
		#filename = dossier
		dossier = "Download all images part1"
		parent_dir = "./"
		path = os.path.join(parent_dir, dossier)
		os.mkdir(path)
		print("le dossier %s a eté crée !" %dossier)
	except:
		pass

	if reponse.ok:	
		soup = BeautifulSoup(reponse.text, "html.parser")
		#print(soup.title.text)
		images = soup.find_all("img")
		#print(images)

		count = 0
		print(f"Total {len(images)} images trouvées !")

	if len(images) != 0:
		for image in tqdm(images):
			imglink = image.attrs.get("src")
			urls = imglink.replace("../../../../", "")
			urls_images = ("http://books.toscrape.com/" + urls)
			print(urls_images)
			image = requests.get(urls_images).content
			filename = dossier + urls_images[urls_images.rfind("/"):]
			#print(filename)

			with open(filename, "wb") as file:
				file.write(image)

			count += 1

	if count == len(images):
		print("Toutes les images ont été téléchargées !")
					             
	else:
		print(f"Total {count} images téléchargées sur {len(images)}")

	print(f"Total {count} images téléchargées")

	print("=============================================================================================================\n")

	#reponse = requests.get(url)
	#page = reponse.content
	urls = []
	pagination_page = True
	count = 1
	while pagination_page:
		reponse = requests.get(url)
		page = reponse.content
		soup = BeautifulSoup(reponse.text, "html.parser")
		current_elements = soup.select_one("li.current")
		print(current_elements.text.strip())
		count += 1

		next_page_elements = soup.select_one("li.next > a")
		if next_page_elements:
			next_page_url = next_page_elements.get("href")
			url = urljoin(url, next_page_url)
			print(url)
			urls.append(url)

		elif soup.find("ul",class_="next") is None:
			pagination_page = False

	for url in urls:
		reponse = requests.get(url)
		page = reponse.content

		try: 
			#filename = dossier
			dossier = "Download all images part2"
			parent_dir = "./"
			path = os.path.join(parent_dir, dossier)
			os.mkdir(path)
			print("le dossier %s a eté crée !" %dossier)
		except:
			pass

		if reponse.ok:
			soup = BeautifulSoup(reponse.text, "html.parser")
			#print(soup.title.text)
			images = soup.find_all("img")
			#print(images)

			count = 0
			print(f"Total {len(images)} images trouvées !")

			if len(images) != 0:
				for image in tqdm(images):
					imglink = image.attrs.get("src")
					urls = imglink.replace("../../../../", "")
					urls_images = ("http://books.toscrape.com/" + urls)
					print(urls_images)
					image = requests.get(urls_images).content
					filename = dossier + urls_images[urls_images.rfind("/"):]
					#print(filename)

					with open(filename, "wb") as file:
						file.write(image)

					count += 1

			if count == len(images):
				print("Toutes les images ont été téléchargées !")
						             
			else:
				print(f"Total {count} images téléchargées sur {len(images)}")

	print(f"Total {count} images téléchargées")

	print("=============================================================================================================\n")


#lancement du programme et du temps d'exécution 
if __name__ == '__main__':

	time_start = datetime.now()

	#lancement extraction des données
	extract_all_data = fonction_main_extract_all_categories("http://books.toscrape.com")

	#écriture des fichiers csv 
	write_file_import_csv(extract_all_data)

	#lancement du download des images 
	download_all_images("http://books.toscrape.com")

	time_end = datetime.now()

	print(time.strftime("%d/%m/%Y"))
	print(time.strftime("%Z"))
	print(f"Temps d'exécution du programme (hh:mm:ss.ms) {time_end - time_start}")


	