from allure_commons.types import Severity

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure

from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTags


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTags.REGRESSION, AllureTags.REGISTRATION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.REGISTRATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.REGISTRATION)
class TestRegistration:
    @allure.title('Check successful registration')
    @allure.severity(Severity.BLOCKER)
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email='user.name@gmail.com',
                                                 username='username', password='password')
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view.check_visible()

