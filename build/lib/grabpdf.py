#
#  getpdf: Simple pdf scraper
#
#  Copyright (c) 2017 Mark Kelly 
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  Requires: Python 2.7/3.3+


__version__ = '0.0.0dev'

import urllib.request
import urllib.parse
import requests
import os
from bs4 import BeautifulSoup as soup 

url = 'http://cs229.stanford.edu/materials.html'
cwd = '/home/kelly/projects/getpdf'
response = urllib.request.urlopen(url)





page = response.read()

data = soup(page)

test1 = data.a

#print(test1)

#print(test1['href'])

links = data.find_all('a', href=True)
#link1 = links.attrs['href']
docs = [urllib.parse.urljoin(url,lnk.attrs['href']) for lnk in links if ".pdf" in str(lnk)]

#print(docs)
print(os.path.basename(docs[0]))

for doc in docs:
	local_filename, headers = urllib.request.urlretrieve(doc, '/home/kelly/projects/getpdf/test' + os.path.basename(doc))
#html = open(local_filename)
#
