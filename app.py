
# Dmytro Honcharenko
# 25 Nov 2021 - Coding Assignment

import os
import re
import requests
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Url:
    def __init__(self, name, url, version=None, hash=None):
        self.name = name
        self.url = url
        self.version = version
        self.hash = hash

#empty array of objects
urlobjs = []

for key in os.environ:
    if "_URL" in key:
        print(f"_URL detected: {key}")
        urlobjs.append( Url(key, os.environ[key]) )

for obj in urlobjs:
    # edge case - try if URL is available and we can pull the data from there
    try:
        r = requests.get(obj.url).json()
    except requests.exceptions.HTTPError as errh:
        print (f"Http Error: {errh} fetching from {obj.url}")
    except requests.exceptions.Timeout as errt:
        print (f"Timeout Error: {errt} fetching from {obj.url} URL")
    except ValueError:
        print(f"{obj.url} JSON decoding has failed for some reason")
        continue
    
    # let's separate hash (md5?) from the version string
    hash = re.search("\(([^\)]+)\)", r["core_version"]).group(0)
    obj.version = r["core_version"]
    obj.hash = hash

for k in urlobjs:
    #lets figure out a branch to compare with
    if "PROD" in k.name:
        mainver = k.version
        print(f"\nmain version: {k.name}: {k.version}\n")

    if k.version != mainver:
        print(f"{k.version} ({k.name}) is not matching main version {mainver}")