class Car:  #Car라는 객체를 만들고, 기능을 정의
    def __init__(self,speed,color,model):   #__init__
        self.speed = speed
        self.color = color
        self.model = model
        
    def drive(self):    #dirve 라는 기능을 정의
        self.speed = 60 #speed를 60으로 정의

    def __str__(self):
        

myCar = Car(0,"blue","E-class")
yourCar = Car(10,"red","S-class")

print("자동차 객체를 생성하였습니다.")
print(myCar.speed)
print(myCar.color)
print(myCar.model)
print(yourCar.speed)
print(yourCar.color)
print(yourCar.model)
print("자동차를 주행합니다.")
myCar.drive()
yourCar.drive()
print(myCar.speed)
print(yourCar.speed)
