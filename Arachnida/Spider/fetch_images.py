from collect_links import extract_image_links, request_page
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

def fetch_all_images(params):


	r = request_page(params["url"])
	images = extract_image_links(r.content, params["url"])
	if not os.path.exists(params["p"]):
		os.makedirs(params["pgit ad"])
	if params["r"] == False:
		fetch_images(images, params)
		
