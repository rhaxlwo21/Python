phone_book = {"유준":"0001","은기":"1111","민영":"2222","주현":"3333","민주":"4444","윤주":"5555"}

print(phone_book["윤주"])
print(phone_book)
print(sorted(phone_book))
print(phone_book)

for key in phone_book.keys():
    print(key)

for key in phone_book.values():
    print(key)

for key in phone_book.keys():
    print(key,phone_book[key])
