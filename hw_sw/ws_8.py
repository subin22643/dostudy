# # ws_8_1.py

# # 아래 클래스를 수정하시오.
# class Animal:
#     num_of_animal = 0

# class Dog(Animal):
#     def __init__(self):
#         Animal.num_of_animal += 1
    

# class Cat(Animal):
#     def __init__(self):
#         Animal.num_of_animal += 1

# class Pet(Dog, Cat):
#     @classmethod
#     def access_num_of_animal(cls):
#         return f'동물의 수는 {cls.num_of_animal}마리 입니다.'
    
# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())





# # ws_8_2.py

# # 아래 클래스를 수정하시오.
# class Animal:
#    pass


# class Dog(Animal):
#     def __init__(self):
#         pass


#     def bark(self):
#         print("멍멍!")


# dog1 = Dog()
# dog1.bark()




# # ws_8_3.py

# # 아래 클래스를 수정하시오.
# class Animal:
#    pass


# class Cat(Animal):
#    def __init__(self):
#         pass

#    def meow(self):
#       print("야옹!")


# cat1 = Cat()
# cat1.meow()





# class Dog:
#     def __init__(self):
#         pass


#     def bark(self):
#         print("멍멍!")



# class Cat:
#    def __init__(self):
#         pass

#    def meow(self):
#       print("야옹!")



# class Pet(Dog, Cat):
    
#     def __init__(self, sound):    # self.sound가 인스턴스 변수
#         self.sound = sound

#     def play(self):
#         print("애완동물과 놀기")

#     def make_sound(self):
#         print(self.sound)


# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()





# class Dog:
#     sound = "멍멍"

# class Cat:
#     sound = "야옹"


# class Pet(Dog, Cat):
    
#     def __init__(self):
#         pass

#     def __str__(self):
#         return f'애완동물은 {self.sound}소리를 냅니다'
    
# pet = Pet()
# print(pet)




# # hw_8_2.py

# # 아래 함수를 수정하시오.
# def check_number():
#     try:
#         num = int(input('숫자를 입력하세요: '))
#         if num > 0:
#             print("양수입니다.")
#         elif num == 0:
#             print("0입니다.")
#         elif num < 0:
#             print("음수입니다.")

#     except ValueError:
#         print("잘못된 입력입니다.")

# check_number()




# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        try:
            user_name = input('이름을 입력하세요: ')

            if user_name != '':
                user_age = int(input('나이를 입력하세요: '))
            else:
                print("사용자 정보가 입력되지 않았습니다.")

        except ValueError:
            print("나이는 숫자로 입력해야 합니다.")
        
        self.user_data = {'name' : user_name, 'age':user_age}

    def display_user_info(self):
        print("사용자 정보:")
        print(f"이름: {self.user_data['name']}")
        print(f"나이: {self.user_data['age']}")


user = UserInfo()
user.get_user_info()
user.display_user_info()