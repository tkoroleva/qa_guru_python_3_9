import datetime
from dataclasses import dataclass


@dataclass
class User:
    name: str
    surname: str
    email: str
    phone_number: str
    address: str
    birthday: datetime.date
    gender: str
    subjects: str
    hobbies: str
    picture: str
    state: str
    city: str


test_user = User(
    name='QA',
    surname='GURU',
    email='test@qa.guru',
    gender='Other',
    phone_number='7999123456',
    birthday=datetime.date(2022, 11, 16),
    subjects='Computer Science',
    hobbies='Reading',
    picture='logo.png',
    address='Russia, Moscow',
    state='Haryana',
    city='Panipat')
