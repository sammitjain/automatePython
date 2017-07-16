# Web scraping with Beautiful Soup 4 Part 3
# Working with tables using pandas

import pandas as pd
import urllib.request
import bs4 as bs

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/',header=0)

for df in dfs:
    print(df)
