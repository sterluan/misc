import urllib2
import urlparse
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = "http://www.bilibili.com/video/movie_west_1.html"
soup = BeautifulSoup(urllib2.urlopen(url))
datastart = soup.find('input', attrs={"class":"range_start"})['value']
dataend = soup.find('input', attrs={"class":"range_end"})['value']
url1 = "http://www.bilibili.com/list/default-145-"
url2 = "-" + datastart + "~" + dataend + ".html"

fp = open('bilibili_movies.txt', 'w+')

# identify the number of pages to explore
num_of_pages = 5
for i in xrange(1, num_of_pages + 1):
    newurl = url1 + str(i) + url2
    #print "newurl:", newurl
    #raw_input()
    htmlfile = urllib2.urlopen(newurl)
    soup = BeautifulSoup(htmlfile)
    links = soup.findAll('a', attrs={"class":"preview"})
    for link in links:
        fullurl = urlparse.urljoin("http://" + urlparse.urlparse(url).hostname, link['href'])
        #print isinstance(link['title'], str)
        #print isinstance(fullurl, str)
        #print isinstance(link['href'], str)
        #print link['title'] + ": " + fullurl
        fp.write(link['title'] + ": " + fullurl + "\n")
        #fp.write(fullurl + "\n")
        
fp.close()
