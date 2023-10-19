from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_registration_student():
    student = User(
        first_name='Vasya',
        last_name='Pupkin',
        email='Pupkin@example.com',
        gender='Male',
        mobile='1234567890',
        dayofbirth='1',
        mohtofberth='September',
        yearofbirth='2000',
        subject='English',
        hobbies='Sports',
        picture='picture.jpeg',
        address='123, Street, City, Country',
        state='NCR',
        city='Delhi'
    )
    registration_page.open()
    registration_page.register_student(student)
    registration_page.should_have_registered(student)
