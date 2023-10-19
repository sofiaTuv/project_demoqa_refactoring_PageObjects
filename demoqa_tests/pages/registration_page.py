from selene.support.shared import browser
from selene import have, command, be
import resource


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.config.driver.maximize_window()
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def register_student(self, user):
        browser.element('#firstName').should(be.visible).type(user.first_name)
        browser.element('#lastName').should(be.visible).type(user.last_name)
        browser.element('#userEmail').should(be.visible).type(user.email)
        browser.all('.custom-radio').element_by(have.text(user.gender)).click()
        browser.element('#userNumber').should(be.visible).type(user.mobile)
        browser.element('#dateOfBirthInput').should(be.visible).click()
        browser.element('.react-datepicker__year-select').type(user.yearofbirth)
        browser.element('.react-datepicker__month-select').type(user.mohtofberth)
        browser.element(f'.react-datepicker__day--00{user.dayofbirth}').click()
        browser.element('#subjectsInput').should(be.visible).type(user.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(user.hobbies)).click()
        browser.element('#uploadPicture').should(be.visible).type(resource.path(user.picture))
        browser.element('#currentAddress').should(be.visible).type(user.address)
        browser.element("#react-select-3-input").should(be.visible).type(user.state).press_enter()
        browser.element("#react-select-4-input").should(be.visible).type(user.city).press_enter()
        browser.element('#submit').perform(command.js.click)

    def should_have_registered(self, user):
        full_name = f'{user.first_name} {user.last_name}'
        stateandcity = f'{user.state} {user.city}'
        dateofbirth = f'{user.dayofbirth} {user.mohtofberth},{user.yearofbirth}'
        browser.element('.table').all('td').even.should(
            have.texts(
                full_name,
                user.email,
                user.gender,
                user.mobile,
                dateofbirth,
                user.subject,
                user.hobbies,
                user.picture,
                user.address,
                stateandcity
            ))
        return self
