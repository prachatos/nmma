from lib import gen_data_for_entries 
import pandas as pd
import os
import configparser

CONFIG_FILENAME = os.path.join('config', 'data-fetch.cfg')

if __name__ == '__main__':
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILENAME, encoding='utf8')
    try:
        filename = config_parser.get('file', 'filename')
    except Exception:
        print("Did not find input filename, exiting.")
        exit(0)
    full_file = os.path.join('lists', filename + '.csv')
    try:
        fr = int(config_parser.get('file', 'from'))
    except Exception:
        fr = 0
    try:
        to = int(config_parser.get('file', 'to'))
    except Exception:
            to = -1 
    try:
        output = config_parser.get('file', 'output') + '.csv'
    except Exception:
        print("Did not find output filename, exiting.")
        exit(0)
    print('Downloading data for', filename)
    gen_data_for_entries(full_file, fr, to, output)
