from allure_commons.types import Severity

from config import settings
from pages.dashboard.dashboard_page import DashboardPage
import pytest
import allure

from tools.allure.epics import AllureEpics
from tools.allure.features import AllureFeatures
from tools.allure.stories import AllureStories
from tools.allure.tags import AllureTags
from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSION, AllureTags.DASHBOARD)
@allure.epic(AllureEpics.LMS)
@allure.feature(AllureFeatures.DASHBOARD)
@allure.story(AllureStories.DASHBOARD)
@allure.parent_suite(AllureEpics.LMS)
@allure.suite(AllureFeatures.DASHBOARD)
@allure.sub_suite(AllureStories.DASHBOARD)
class TestDashboard:
    @allure.title('Check displaying of dashboard page')
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.scores_chart_view.check_visible(title="Scores")
        dashboard_page_with_state.courses_chart_view.check_visible(title="Courses")
        dashboard_page_with_state.students_chart_view.check_visible(title="Students")
        dashboard_page_with_state.activities_chart_view.check_visible(title="Activities")