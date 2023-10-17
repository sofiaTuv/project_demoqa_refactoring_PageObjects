from demoqa_tests.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Vasya').fill_last_name('Pupkin')
    registration_page.fill_email('Pupkin@example.com')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile_number('1234567890')
    registration_page.fill_date_of_birth('1', 'September', '2000')
    registration_page.fill_subjects('English')
    registration_page.fill_hobbies('Sports')
    registration_page.fill_upload_picture('picture.jpeg')
    registration_page.fill_address('123, Street, City, Country')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Noida')
    registration_page.submit_click()

    registration_page.should_registered_user_with(
        'Vasya Pupkin',
        'Pupkin@example.com',
        'Male',
        '1234567890',
        '01 September,2000',
        'English',
        'Sports',
        'picture.jpeg',
        '123, Street, City, Country',
        'NCR Noida',
    )
