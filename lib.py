import urllib.request
import requests
from lxml import html
import pandas as pd
import re, unicodedata

BASE_URI = "http://nmma.nic.in/nmma/"

def gen_state_entries(state, url, max_count):
    d = []
    cur = 0
    while cur < max_count:
        page = requests.get(BASE_URI + url + "&pager.offset=" + str(cur))
        tree = html.fromstring(page.content)
        links = tree.find_class('text-style-4')
        for l in links:
            content = l.cssselect('td')
            acc_no = content[1].text_content()
            cont_url = content[0].cssselect('a')[0].get('href')
            name = content[0].text_content()
            d.append([acc_no, name, cont_url])
        cur += 50
    df = pd.DataFrame(d, columns=["ref no", "name", "url"])
    df.to_csv(open(state.replace(" ", "") + "-list.csv", "w+"), index=False)
    return
   
def remove_nonlatin(s): 
    new_s = ""
    for ch in s:
        try:
            if unicodedata.name(ch).startswith(('LATIN', 'DIGIT', 'SPACE', 'SOLIDUS', 'HYPHEN')):
                new_s += ch
        except Exception:
            continue
    new_s = ''.join(new_s)
    new_s = new_s.strip()
    new_s = new_s.strip('/')
    new_s = new_s.strip('-')
    new_s = new_s.strip()
    new_s = new_s.strip('/')
    new_s = new_s.strip('-')
    new_s = new_s.replace(',', '-')
    new_s = new_s.strip()
    return new_s

def gen_data_for_entries(csvdat, fr, to, filename):
    d = []
    df = pd.read_csv(csvdat)
    all_rows = df.iterrows()
    count = 0
    for index, row in all_rows:
        if count < fr or count > to:
            count += 1
            continue
        url = str(row[2])
        name = str(row[1])
        url_full = str(BASE_URI) + str(url)
        page = requests.get(url_full)
        tree = html.fromstring(page.content)
        link_p = tree.cssselect('table')[0].cssselect('tr')
        data = dict()
        data["Name"] = name
        for a in link_p:
            td = a.cssselect('td')
            if len(td) == 1:
                continue
            ind, val = td
            ind = remove_nonlatin(str(ind.text_content()).strip())
            val = remove_nonlatin(str(val.text_content()).strip())
            if len(val) > 0:
                data[ind] = val
        d.append(data)
        count += 1
    pd_df = pd.DataFrame(d)
    pd_df.to_csv(filename + '.csv', index=False)
    return pd_df
