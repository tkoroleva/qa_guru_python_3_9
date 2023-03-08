from selene import have
from selene.support.shared import browser
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.radiobutton import Radiobutton
from demoqa_tests.utils import date_config
from demoqa_tests.utils.path_to_file import define_path
from demoqa_tests.utils.scroll import scroll_to


class PracticeForm:
    def __init__(self, user):
        self.user = user

    def open_page(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.6)"')
        return self

    def input_name(self):
        browser.element('#firstName').type(self.user.name)
        browser.element('#lastName').type(self.user.surname)

    def input_contacts(self):
        browser.element('#userEmail').type(self.user.email)
        browser.element('#userNumber').type(self.user.phone_number)

    def select_gender(self):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_by_value(self.user.gender)

    def select_birthday(self):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set_date(self.user.birthday)

    def input_subjects(self):
        browser.element('#subjectsInput').type(self.user.subjects).press_enter()

    def select_hobbies(self):
        check_hobbies = Checkbox(browser.all('[for^=hobbies-checkbox]'))
        check_hobbies.select(self.user.hobbies)

    @staticmethod
    def scroll_to_address():
        scroll_to('#currentAddress')

    @staticmethod
    def upload_picture():
        browser.element('#uploadPicture').set_value(define_path())

    def input_address(self):
        browser.element('#currentAddress').type(self.user.address)

    def select_state(self):
        dropdown = Dropdown('#state')
        dropdown.select(self.user.state)

    def select_city(self):
        dropdown = Dropdown('#city')
        dropdown.select(self.user.city)

    @staticmethod
    def submit():
        browser.element('#submit').press_enter()

    def fill_form(self):
        self.open_page()
        self.input_name()
        self.input_contacts()
        self.select_gender()
        self.select_birthday()
        self.input_subjects()
        self.select_hobbies()
        self.scroll_to_address()
        self.upload_picture()
        self.input_address()
        self.select_state()
        self.select_city()
        self.submit()

    def check_fields(self):
        browser.element('.table').all('td').even.should(have.texts(
            self.user.name + ' ' + self.user.surname,
            self.user.email,
            self.user.gender,
            self.user.phone_number,
            self.user.birthday.strftime(date_config.datetime_view_format),
            self.user.subjects,
            self.user.hobbies,
            self.user.picture,
            self.user.address,
            self.user.state + ' ' + self.user.city))
