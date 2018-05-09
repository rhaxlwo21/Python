def cal_area(radius):
    area = 3.14*radius**2
    return area

user = int(input("반지름을 입력하세요:"))

c_area = cal_area(user)

print("원의 넓이는 :",c_area)
