import book

def rental_book(name, books):
    result = book.decrease_book(books)

    print(f'남은 책의 수 : {result}')
    print(f'{name}님이 {books}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)