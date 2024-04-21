from bs4 import BeautifulSoup
import requests

# soup.find_all('img')  find all occurances of img and return it in a list
#soup.find(id="hello")  find something by it's id


"""
Steps for images fetching:
1-fetch the webpage
2-convert it ot text
3-Extract images links
4-If no recursion fetch all images
5-else Extract links
6-Fetch as per layers

"""
def	request_page(url):
	return requests.get(url, timeout=10)


def	get_links_in_page(url):
	r = requests.get(url, timeout=10)
	soup = BeautifulSoup(r.text, 'html.parser')
	link_layer = []
	for links in soup.find_all('a'):
		single_link = links.get('href')
		try:
			if single_link[0] == '/':
				single_link = url + single_link
			link_layer.append(single_link)
		except Exception as e:
			print(e)
	return link_layer


# def	fetch_images(image_links, offset_name):
# 	x = 0
# 	for image_url in image_links:
# 		r = requests.get(image_url, timeout=2)
# 		filename = "./data/" + offset_name +  "_"+ str(x) +".jpg"
# 		with open(filename, 'wb') as fd:
# 			for chunk in r.iter_content(chunk_size=128):
# 				fd.write(chunk)
# 		x += 1

# def	collect_links(url):
# 	r = request_page(url)
# 	soup = BeautifulSoup(r.text, 'html.parser')
# 	link_layer = []
# 	for links in soup.find_all('a'):
# 		single_link = links.get('href')
# 		try:
# 			if single_link[0] == '/':
# 				single_link = url + single_link
# 			link_layer.append(single_link)
# 		except Exception as e:
# 			print(e)
# 	return link_layer

def extract_image_links(request_text, url):
	soup = BeautifulSoup(request_text, 'html.parser')
	images = soup.find_all('img')
	image_links = []
	for image in images:
		try:
			image_link = image.get('src')
			if image_link[0] == "/" or image_link[0] == "." or image_link[0] != "h":
				image_link = url + image_link
			
			image_links.append((image_link, get_img_extension(image_link)))
				
		except Exception as e:
			pass
	return image_links

def	get_img_extension(link):
	if ".jpg" in link:
		return ".jpg"
	elif (".jpeg") in link:
		return 'jpeg'
	elif (".png") in link:
		return '.png'
	elif (".gif") in link:
		return '.gif'
	elif (".bmp") in link:
		return '.bmp'
	else:
		raise NameError("Non supported extension by default")
	