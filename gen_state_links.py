from lib import gen_state_entries 
import pandas as pd
import os
import configparser

CONFIG_FILENAME = os.path.join('config', 'state.cfg')

if __name__ == '__main__':
	config_parser = configparser.ConfigParser()
	config_parser.read(CONFIG_FILENAME, encoding='utf8')
	try:
		filename = config_parser.get('file', 'filename') + ".csv"
	except Exception:
		filename = "nmma-states.csv"
	filename = os.path.join('lists', filename)
	try:
		indices = [int(i) for i in config_parser.get('file', 'indices').split(',')]
	except Exception:
		indices = []
	pd_df = pd.read_csv(filename)
	for index, row in pd_df.iterrows():
		if not len(indices) or int(row[0]) in indices:
			print('Downloading links for', row[1])	
			state = row[1]
			url = row[2]
			max_count = row[3]
			gen_state_entries(state, url, max_count)
