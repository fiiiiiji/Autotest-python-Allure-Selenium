"""
Test Smoke
"""
from selenium.webdriver.common.by import By
from conftest import browser

URL = "https://testqastudio.me/"

def test_main(browser):
    """
    SMK-1. Test Smoke
    """
    browser.get(URL)

    element = browser.find_element(by=By.CSS_SELECTOR, value="#main > div.catalog-toolbar.layout-v3 > div.catalog-toolbar-tabs__content > a.tab-featured")
    element.click()
    element = browser.find_element(by=By.CSS_SELECTOR, value="#rz-shop-content > ul > li.layout-v2.product-thumbnails-vertical.product-add-to-cart-ajax.razzi-play-video--popup.product.type-product.post-11341.status-publish.first.instock.product_cat-122.product_tag-121.product_tag-141.product_tag-135.product_tag-124.product_tag-142.has-post-thumbnail.featured.shipping-taxable.purchasable.product-type-simple > div > div.product-summary > h2 > a")
    element.click()
    element = browser.find_element(by=By.CSS_SELECTOR, value="#product-11341 > div.product-gallery-summary.clearfix > div.summary.entry-summary > div.product_meta > span.sku_wrapper > span.sku")

    assert element.text == "C0MSSDSUM7"
