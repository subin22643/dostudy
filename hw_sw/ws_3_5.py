import book

number_of_people = 0

def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {'name': name, 'age': age, 'address': address}

user_information = map(create_user, name, age, address)

many_user = list(user_information)


def rental_book(info):
    pass
