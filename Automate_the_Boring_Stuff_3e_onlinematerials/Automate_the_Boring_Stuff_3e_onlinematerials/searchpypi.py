# searchpypi.py - Opens several search results on pypi.org

import requests, sys, webbrowser, bs4

print('Searching...')  # Display text while downloading the search result page.
res = requests.get('http://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features='html.parser')
link_elems = soup.select('.package-snippet')
numOpen = min(5, len(link_elems))
for i in range(numOpen):
    urlToOpen = 'http://pypi.org' + link_elems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
