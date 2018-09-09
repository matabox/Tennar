#!/usr/bin/env python

import requests
import re
import time
import hashlib
import os
import random
import shutil
import copy

def main():

	urls = [
		"https://www.fiverr.com/stephanton/design-a-modern-esports-logo",
		"https://www.fiverr.com/stephanton/design-unique-twitch-overlay-and-esports-logo",
		"https://www.fiverr.com/evanurula/design-gaming-esports-logo-97b21b9a-82f9-42ba-acc9-3f899b8bd11e",
		"https://www.fiverr.com/bnxkt15/design-you-professional-sport-esport-character-mascot-logo-for-you"
	]

	regexString = r'original":"(.*?)"}}'

	headers = {
		"User-Agent" : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36"
	}

	for url in urls:

		print "[!] Trying to process URL: %s" % (url)

		requestData = requests.get(url, headers=headers)

		images = re.findall(regexString, requestData.text)

		counter = 1

		for image in images:

			print "[+] Downloading image: %s of %s" % (counter, len(images))

			rtime = random.uniform(1.0, 3.0)

			print "[!] Sleeping for a random amount of time, this time was: %s" % (rtime)

			time.sleep(rtime)

			imageData = requests.get(image, headers=headers, stream=True)
			hashData = requests.get(image, headers=headers, stream=True)
			
			if not os.path.exists("images"):
				os.makedirs("images")

			if not os.path.exists("images/" + url.rsplit('/', 1)[1]):
				os.makedirs("images/" + url.rsplit('/', 1)[1])

			md5 = "images/" + url.rsplit('/', 1)[1] + "/" + hashlib.md5(hashData.text.encode('utf-8')).hexdigest()
			#md5 = "images/" + url.rsplit('/', 1)[1] + "/" + hashlib.md5(str(random.uniform(1.0, 5.0))).hexdigest()

			if os.path.exists(md5):
				print "[-] Already downloaded this image"
			else:
				print "[+] New image downloaded"
				with open(md5, "wb") as out_file:
					shutil.copyfileobj(imageData.raw, out_file)
				del imageData
				
			counter = counter + 1

		#print requestData.text

if __name__ == '__main__':
	main()
