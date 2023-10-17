from pathlib import Path

from selene import have, command
from selene.support.shared import browser

import tests


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('label[for="gender-radio-1')
        self.user_mobile = browser.element('#userNumber')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element('//label[. ="Sports"]')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.state_select = browser.element('#react-select-3-input')
        self.city = browser.element('#city')
        self.city_select = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.config.driver.maximize_window()
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_gender(self, value):
        self.gender.should(have.text(f'{value}')).click()
        return self

    def fill_mobile_number(self, value):
        self.user_mobile.type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(month)
        self.date_of_birth_year.type(year)
        browser.element(
            f'.react-datepicker__day--00{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        self.subjects_input.type(f'{value}').press_enter()
        return self

    def fill_hobbies(self, value):
        self.hobbies.should(have.text(value)).click()
        return self

    def fill_upload_picture(self, value):
        p = str(Path(tests.__file__).parent.joinpath(f'resources/{value}').absolute())
        self.picture.set_value(p)
        return self

    def fill_address(self, value):
        self.address.type(value)

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)).click()
        return self

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)).click()
        return self

    def submit_click(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_registered_user_with(self, studentname, studentemail, gender, mobile, dateofbirth, subjects, hobbies,
                                    picture, address, stateandcity):
        browser.element('.table').all('td').even.should(
            have.texts(
                studentname,
                studentemail,
                gender,
                mobile,
                dateofbirth,
                subjects,
                hobbies,
                picture,
                address,
                stateandcity,
            )
        )
        return self
