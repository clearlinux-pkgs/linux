#!/usr/bin/python3

import json

with open("releases.json", "r", encoding="latin-1") as myfile:
    data = json.load(myfile)

if "latest_stable" not in data:
    exit(40)

stable = data["latest_stable"]
version = stable['version']
halfversion = version[:5]

regexp = "s/" + halfversion.replace(".", "\\.") + "[0-9]*/" + version.replace(".", "\\.") + "/g"

print(regexp)
