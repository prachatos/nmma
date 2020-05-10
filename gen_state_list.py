import urllib.request
import requests
from lxml import html
import pandas as pd
import re

BASE_URI = "http://nmma.nic.in/nmma/"

def gen_state_list():
    page = requests.get(BASE_URI + "exploreBuilt.do")
    tree = html.fromstring(page.content)
    links = tree.find_class('tab-content')[1].cssselect('a')
    d = []
    for l in links:
        state_name, entries = l.text_content().split("(")
        entries = entries.replace(")", "")
        d.append([state_name, l.get('href'), entries])
    df = pd.DataFrame(d, columns=["state", "url", "entries"])
    df.index.name = "index"
    df.to_csv(open("nmma-states.csv", "w+"))
    return
