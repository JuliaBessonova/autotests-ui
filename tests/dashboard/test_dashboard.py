from pages.dashboard.dashboard_page import DashboardPage
import pytest

@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible("username")
        dashboard_page_with_state.dashboard_toolbar_view.check_visible()
        dashboard_page_with_state.scores_chart_view.check_visible(title="Scores")
        dashboard_page_with_state.courses_chart_view.check_visible(title="Courses")
        dashboard_page_with_state.students_chart_view.check_visible(title="Students")
        dashboard_page_with_state.activities_chart_view.check_visible(title="Activities")