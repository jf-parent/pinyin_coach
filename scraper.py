#!/usr/bin/env python

import base64
import os

import requests
from bs4 import BeautifulSoup
from IPython import embed


HERE = os.path.abspath(os.path.dirname(__file__))
sound_dir = os.path.join(HERE, 'sound')
if not os.path.exists(sound_dir):
    os.makedirs(sound_dir)
    print "Sound directory created: %s"%sound_dir

url = base64.b64decode("aHR0cDovL3d3dy55b3lvY2hpbmVzZS5jb20vY2hpbmVzZS1sZWFybmluZy10b29scy9NYW5kYXJpbi1DaGluZXNlLXByb251bmNpYXRpb24tbGVzc29uL3Bpbnlpbi1jaGFydC10YWJsZQ==")
doc = requests.get(url)
print "Pinyin file list fetched"

soup = BeautifulSoup(doc.text, 'html.parser')

sound_list = soup.find_all("div", class_="chart-audio")

for sound in sound_list:
    file_name = sound.attrs['path'].split('/')[-1]
    file_path = os.path.join(HERE, sound_dir, file_name)

    response = requests.get(sound.attrs['path'], stream=True)
    print "Fetching: %s"%file_name

    if not os.path.exists(file_path):
        with open(file_path, 'wb') as fd:
            for block in response.iter_content(1024):
                fd.write(block)

print "Done!"
