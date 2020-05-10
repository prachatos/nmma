# nmma
Tool to scrape data from NMMA for use in Wikimedia projects (Wikidata)

# Scripts
This repository has 3 scripts - one for generating list of all states (not neccessary to use), one for generating links for sites for each state and the third for actually downloading data in a CSV file.

# Installation
- Python 3.6
- Clone repo
- pip install -r requirements.txt 

# Generating list of states

- *python gen_state_list.py <optional filename>*

# Generating links for all entities in a state

- This relies on the **config/state.cfg** file. The first parameter is the state CSV generated in the first step and the second is a list of indices of states to fetch data from.
- *python gen_state_links.py*
- This generates a set of files using the state name, all saved to *lits/xyz.csv*. These files are required to actually generate CSV containing data.

# Generating CSV with data of items

- This relies on the **config/data-fetch.ini** file. The first parameter is the state link CSV generated in the second step. From and To are optional indices from the input CSV from where data should be fetched. The last is the filename for ouput CSV.
- *python gen_data.py*
- This generates a set of CSVs that contain data for all items in a state.
