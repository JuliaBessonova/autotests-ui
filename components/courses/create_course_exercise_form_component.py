from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text
import allure


class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.delete_exercise_button = Button(page, 'create-course-exercise-{index}-box-toolbar-delete-exercise-button',
                                             'Delete exercise')
        self.exercise_subtitle = Text(page, 'create-course-exercise-{index}-box-toolbar-subtitle-text',
                                      'Exercise subtitle')
        self.exercise_title_input = Input(page, 'create-course-exercise-form-title-{index}-input', 'Title')
        self.exercise_description_input = Input(page, 'create-course-exercise-form-description-{index}-input',
                                                'Description')


    def click_delete_button(self, index: int):
        self.delete_exercise_button.click(index=index)


    @allure.step('Check visible create course exercise form at index "{index}"')
    def check_visible(self, index: int, title: str, description: str):
        self.exercise_subtitle.check_visible(index=index)
        self.exercise_subtitle.check_have_text(f"#{index + 1} Exercise", index=index)

        self.exercise_title_input.check_visible(index=index)
        self.exercise_title_input.check_have_value(title, index=index)

        self.exercise_description_input.check_visible(index=index)
        self.exercise_description_input.check_have_value(description, index=index)


    @allure.step('Fill create course exercise form at index "{index}"')
    def fill(self, index: int, title: str, description: str):
        self.exercise_title_input.fill(title, index=index)
        self.exercise_title_input.check_have_value(title, index=index)

        self.exercise_description_input.fill(description, index=index)
        self.exercise_description_input.check_have_value(description, index=index)