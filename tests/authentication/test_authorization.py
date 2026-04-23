from allure_commons.types import Severity

from pages.authentication.login_page import LoginPage
import pytest
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure

from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTags



@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTags.REGRESSION, AllureTags.AUTHORIZATION)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.AUTHENTICATION)
@allure.story(AllureStories.AUTHORIZATION)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.AUTHENTICATION)
@allure.sub_suite(AllureStories.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title('Check user login with wrong email or password')
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()


    @allure.title('Check user login with correct email and password')
    @allure.tag(AllureTags.USER_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
            login_page: LoginPage
    ):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.login_form.fill(email='user.name@gmail.com', password='password')
        login_page.click_login_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
        dashboard_page.navbar.check_visible('username')
        dashboard_page.sidebar.check_visible()


    @allure.title('Navigation from login page to registration page')
    @allure.tag(AllureTags.NAVIGATION)
    @allure.severity(Severity.NORMAL)
    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        login_page.click_registration_link()

        registration_page.registration_form.check_visible(email='', username='', password='')
