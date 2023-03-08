from demoqa_tests.model.data.user_data import test_user
from demoqa_tests.model.pages.practice_form import PracticeForm


def test_registration_user():
    practice_form = PracticeForm(test_user)
    practice_form.fill_form()
    practice_form.check_fields()
