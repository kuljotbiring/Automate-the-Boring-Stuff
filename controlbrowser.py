from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a:nth-child(1)')

# will simulate clicking on the element we just grabbed
elem.click()

searchElem = browser.find_element_by_css_selector('insert css selector of unique css for search bar')

# now we can input any string
searchElem.send_keys('hello')
# now submit the search
searchElem.submit()

# press button on browser forward, back, refresh, quit etc
browser.back()
browser.forward()
browser.refresh()
browser.quit()