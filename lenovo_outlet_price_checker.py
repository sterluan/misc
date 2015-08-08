from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS()
url = "http://outlet.lenovo.com/outlet_us/laptops/?menu-id=laptops#facet-1=1,2,3,4&facet-2=1&facet-6=1"
url2 = "http://en.wikipedia.org"
driver.get(url)

for i in xrange(20):
    driver.execute_script('window.scrollBy(0, 400)')
    time.sleep(.5)

price_lists = driver.find_elements(By.XPATH, "//dd[contains(concat(' ', @class, ' '), ' aftercoupon ') and contains(concat(' ', @class, ' '), ' pricingSummary-details-final-price ')]")
model_lists = driver.find_elements(By.XPATH, "//h3/a[contains(concat(' ', @class, ' '), ' facetedResults-cta ') and contains(concat(' ', @class, ' '), ' modeldetailslink ')]")
cpu_lists = driver.find_elements(By.XPATH, "//div[@class='facetedResults-feature-list']/dl[position() = 2]/dd")
    
with open('laptop_lists', 'w') as f:
    for i in xrange(len(model_lists)):
        f.write(model_lists[i].text + ', ' + cpu_lists[i].text + ', ' + price_lists[i].text + '\n')
driver.close()