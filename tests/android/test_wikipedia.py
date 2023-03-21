from selene import have, be
from selene.support.shared import browser
from allure import step as title

from mobile_tests.model import app


def test_search_browser_stack():
    app.given_opened()

    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)


def test_search_js():
    app.given_opened()

    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('JavaScript')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«High-level programming language»').should(be.visible)


def test_search_baku():
    app.given_opened()

    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('Baku')

    with title('Verify content found'):
        browser.all('#page_list_item_description').should(have.size_greater_than(0))
        browser.element('«Capital of Azerbaijan»').should(be.visible)


def test_language_selection():
    app.given_opened()

    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('Baku')

    with title('Open page'):
        browser.element('«Capital of Azerbaijan»').tap()
        browser.element('«Baku»').should(be.visible)

    with title('Language selection'):
        browser.element('Language').tap()
        browser.element('Search for a language').tap()
        browser.element('#search_src_text').type('russian')
        browser.element('#localized_language_name').tap()

    with title('Language change check'):
        browser.element('«Баку»').should(be.visible)
