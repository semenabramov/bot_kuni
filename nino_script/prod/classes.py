class Image:
    def __init__(self,name,acc,freq,time=0,cond = True):
        self.name = name
        self.acc = acc
        self.freq = freq
        self.time = time
        self.cond = cond
        
class Event:
    def __init__(self,name,param):
        self.name = name
        self.param = param  

class Click(Event):
    def __init__(self,name,point):

        self.name = name
        self.point = point    

class Point:
    def __init__(self,mas):
        if(mas==None):
            self.x = None
            self.y = None
        else:
            self.x = mas[0]
            self.y = mas[1]
