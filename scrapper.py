import urllib2
from bs4 import BeautifulSoup
import pdb
#pdb.set_trace()
soup = BeautifulSoup(urllib2.urlopen('http://www.bcsfootball.org').read())
soup = BeautifulSoup(urllib2.urlopen('http://www.wsj.com').read())
pdb.set_trace()
for row in soup('table', {'class': 'mod-data'})[0].tbody('tr'):
	tds = row('td')
	print tds[0].string, tds[1].string

