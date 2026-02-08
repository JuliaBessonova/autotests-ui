from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):

    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    page_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(page_title).to_be_visible()
    expect(page_title).to_have_text('Courses')

    empty_page_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_page_icon).to_be_visible()

    empty_block_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_block_text).to_be_visible()
    expect(empty_block_text).to_have_text('There is no results')

    empty_block_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_block_description).to_be_visible()
    expect(empty_block_description).to_have_text('Results from the load test pipeline will be displayed here')
