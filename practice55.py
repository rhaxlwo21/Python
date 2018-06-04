#TV객체 - 전원 on,off - 채널값 조정
class Tv:
    def __init__(self):
        self.channel = 1
        print("기본 셋팅 번호:",self.channel)

    def powerOn(self):
        print("전원이 켜집니다.")
    def powerOff(self):
        print("전원이 꺼집니다.")
    def channelUp(self):
        if self.channel < 100:
            self.channel += 1
            print("현재 채널 :",self.channel)
    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1
            print("현재 채널 :",self.channel)
            
myTv = Tv()
myTv.powerOn()
myTv.channelUp()
myTv.channelUp()
myTv.channelDown()
myTv.channelDown()
myTv.channelDown()
myTv.powerOff()
