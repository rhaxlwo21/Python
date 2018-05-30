class Car:  #Car라는 객체를 만들고, 기능을 정의
    def drive(self):    #dirve 라는 기능을 정의
        self.speed = 60 #speed를 60으로 정의

myCar = Car()   #Car 라는 객체로 myCar 인스턴스를 만든다.
yourCar = Car()
#myCar 라는 인스턴스가 만들어지고,
#myCar 는 drive()라는 메소드(행동), speed 라는 값을 갖는다.

myCar.speed = 70     #speed 변수값은 0
yourCar.speed = 80
#myCar.model = "E-Class"
#myCar.color = "blue"
#myCar.year = "2017"

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 속도는", yourCar.speed)
#print("자동차의 색상은",myCar.color)
#print("자동차의 모델은", myCar.model)
#print("자동차를 주행합니다.")
#myCar.drive()
#print("자동차의 속도는", myCar.speed)
