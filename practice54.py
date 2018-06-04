#class, __str__, self, 속도증가 객체, 표
class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self):
        self.speed = 60

    def __str__(self):
        msg = "속도:"+str(self.speed)+"/색상:"+str(self.color)+"/모델:"+str(self.model)
        return msg

    def speedUp(self):
        self.speed +=10
        print("속도 증가, 현재속도:",self.speed)

dadCar = Car(0,"silver","A6")
momCar = Car(0,"white","520d")
myCar = Car(0,"blue","E-class")

momCar.speedUp()
momCar.speedUp()
