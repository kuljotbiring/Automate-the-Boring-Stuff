# import beautiful soup  and requests third party module
import bs4, requests


def getAmazonPrice(productUrl):
    res = requests.get(productUrl)

    # check if there are any errors downloading the page
    res.raise_for_status()

    # use beautiful soup function on the webpage text which is in res.txt. returns a beautiful soup object
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # get the html selector - inspect element on page and then copy CSS Path - use that as argument
    elems = soup.select('html.a-ws.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember body.a-m-us.a-aui_72554-c.a-aui_mm_desktop_exp_291916-c.a-aui_mm_desktop_launch_291918-c.a-aui_mm_desktop_targeted_exp_291928-t1.a-aui_mm_desktop_targeted_launch_291922-t1.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_preload_261698-c.a-aui_rel_noreferrer_noopener_309527-c.a-aui_tnr_v2_180836-c div#a-page div#dp.book.en_US div#dp-container.a-container div#rightCol div#desktop_buybox.celwidget div#buybox div#desktop_accordion.celwidget div#accordionRows_feature_div.a-section.a-spacing-none div#accordionRows.celwidget div#buyBoxAccordion.a-box-group.a-accordion.a-spacing-large div#newAccordionRow.a-box.a-accordion-active.celwidget div.a-box-inner.a-accordion-row-container div.a-accordion-row-a11y a.a-accordion-row.a-declarative.accordion-header h5 div#buyNew_cbb div.a-row div.a-column.a-span6.a-text-right.a-span-last span#newBuyBoxPrice.a-size-base.a-color-price.header-price.a-text-normal')

    # select will return a list of all element object of matching elements
    # get the text value we wanted and use strip to take out white spaces
    return elems[0].txt.strip()


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922')
print('the price is ' + price)





