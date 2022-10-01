
#!/usr/bin/env python3

import requests
import unicodedata
import re
import json 
from os.path import exists

# The userid you would like to download from:
USER_ID=""
# The session id of ou logged in, starts with eyJ:
SESSION_TOKEN=""


def main():
	global SESSION_TOKEN, USER_ID
	if not len(SESSION_TOKEN):
		SESSION_TOKEN = input("What is your MidJourney Session ID? (hint: it starts with eyJ and you get it from your browser): ")

	cookies = {'__Secure-next-auth.session-token': SESSION_TOKEN}
	page = 1
	totalImages = 0 
	while(True):
		r = requests.get("https://www.midjourney.com/api/app/recent-jobs/?orderBy=new&jobStatus=completed&userId="+USER_ID+"&dedupe=true&refreshApi=0&page="+str(page), cookies=cookies)
		for render in r.json():
			dex = 0
			foundImage = 0
			if 'image_paths' in render:
				renderName = slugify(render['full_command'])
				write_json(render, renderName+".json")
				# download_image("https://mj-gallery.com/"+render['id']+"/grid_0.png",renderName+"_hq.png")
				for image in render['image_paths']:
					print("Syncing: " + str(totalImages) + ") -> "+ render['full_command'])
					download_image(image, renderName+str(dex)+".png")
					dex += 1
					foundImage += 1
					totalImages += 1
		# no images left.
		if foundImage == 0:
			break
		page += 1;

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    # remove urls
    value = re.sub(r'http\S+', '', value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    ret = re.sub(r'[-\s]+', '-', value).strip('-_')
    return ret[0:248]

def write_json(obj, path):
	# only sync new files.
	if not exists(path):	
		info = open(path,"w")
		info.write(json.dumps(obj))
		info.close()

def download_image(url, path):
	# only sync new files.
	if not exists(path):
		r = requests.get(url, stream=True)
		if r.status_code == 200:
			with open(path, 'wb') as f:
				for chunk in r:
					f.write(chunk)

if __name__ == "__main__":
	main()