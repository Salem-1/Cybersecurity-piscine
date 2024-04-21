from collect_links import *
import requests
from datetime import datetime
import os



def	fetch_images(image_links, params):
	for image in image_links:
		r = requests.get(image[0], timeout=2)
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		filename = f"image_{timestamp}.png"
		filename = params["p"] + "/" + timestamp +image[1]
		
		with open(filename, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)


def	extract_images_one_iteration(url, offset_name):
	r = requests.get(url, timeout=2)
	image_links = extract_image_links(r.text)
	fetch_images(image_links, offset_name)

def	fetch_images_recursively(links, params,recursions):
	if recursions < 1:
		return
	print ("we are in ", recursions)
	for link in links:
		try:
			r = requests.get(link, timeout=5)
			images = extract_image_links(r.content, link)
			fetch_images(images, params)
			new_links = get_links_in_page(link)
			print(links)
			fetch_images_recursively(new_links, params,recursions - 1)
		except Exception as e:
			print(e)
			continue
	print (f"this is the {recursions} iteration ")
	return fetch_images_recursively(links, params,recursions - 1) 

def fetch_all_images(params):


	r = request_page(params["url"])
	images = extract_image_links(r.content, params["url"])
	if not os.path.exists(params["p"]):
		os.makedirs(params["p"])
	fetch_images(images, params)
	if params["r"] == False:
		return
	recursions = params["l"]
	links = get_links_in_page(params["url"])
	fetch_images_recursively(links, params,recursions)		
