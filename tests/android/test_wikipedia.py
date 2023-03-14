from selene import have, be
from selene.support.shared import browser
from allure import step as title


def test_search_browser_stack():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)


def test_search_js():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('JavaScript')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«High-level programming language»').should(be.visible)
