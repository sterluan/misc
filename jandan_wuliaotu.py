from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os
from urllib import urlretrieve

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS()
baseUrl = 'http://jandan.net/pic'
driver.get(baseUrl)

page_str = driver.find_element(By.XPATH, "//span[@class='current-comment-page']").text
page = re.match(r'\[(.*)\]', str(page_str)).groups()[0]
page = int(page)

# number of pages to scrape
pages_to_scrape = 3
img_links = []
for i in xrange(pages_to_scrape):
    url = baseUrl + '/page-' + str(page)
    page -= 1
    driver.get(url)
    imgs = driver.find_elements(By.XPATH, "//p/img")
    for j in xrange(len(imgs)):
        if imgs[j].get_attribute('org_src') is not None:
            img_link = imgs[j].get_attribute('org_src')
        else:
            img_link = imgs[j].get_attribute('src')
        img_links.append(img_link)
        
if not os.path.exists('wuliaotu'):
    os.mkdir('wuliaotu')
os.chdir('wuliaotu')

for i in range(len(img_links)):
    filename = img_links[i].split('/')[-1]
    urlretrieve(img_links[i], filename)