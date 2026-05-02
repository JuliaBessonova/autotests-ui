import pytest
import allure
from allure_commons.types import Severity

from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTags
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTags.REGRESSION, AllureTags.COURSES)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.COURSES)
@allure.story(AllureStories.COURSES)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.COURSES)
@allure.sub_suite(AllureStories.COURSES)
class TestCourses:
    @allure.title('Check empty courses page')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()


    @allure.title('Create new course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title='', description='',
                                                            estimated_time='', min_score='0', max_score='0')
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title="Playwright", estimated_time="2 weeks",
                                                   description="Playwright", max_score="100", min_score="10")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0, title="Playwright", estimated_time="2 weeks",
                                                    min_score="10", max_score="100")


    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title="Playwright", estimated_time="2 weeks",
                                                   description="Playwright", max_score="100", min_score="10")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0, title="Playwright", estimated_time="2 weeks",
                                                    min_score="10", max_score="100")
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.create_course_form.fill(title="Selenium", estimated_time="4 weeks",
                                                   description="Selenium", max_score="200", min_score="50")
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0, title="Selenium", estimated_time="4 weeks",
                                                    min_score="50", max_score="200")





