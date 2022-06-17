import pyautogui
from classes import *
import time

def check(name,arr):
    for i in arr:
        if(name == i.name):
            return True
    return False

def get_loc(name,acc=0.7):
    loc_arrow_cent = None
    loc_arrow = pyautogui.locateOnScreen(f'''../image/{name}''', confidence=acc)
    if(loc_arrow!=None):
        loc_arrow_cent = pyautogui.center(loc_arrow)
    
    return loc_arrow_cent

def find(arr):
    events = []
    for img in arr:
        if (img.cond == False):
            continue
        
        if((time.time()-img.time) >= img.freq):
            img.time = time.time()

            point = Point(get_loc(img.name,img.acc))
            ev = Click(img.name,point)
            if (ev.point.x==None):
                continue

            if(ev.name =='arrow.png'): #Если стрелочка то сразу возвращает только её
                return [ev]

            activation(img,arr)
            
            
            events.append(ev)

    return events    

def filter(events):
    for ev in events:

        
        if(ev.name == 'learn_right_bottom.png'):
            pyautogui.click(ev.point.x+50,ev.point.y+50)
            events.remove(ev)
        
        if(ev.name == 'learn_left_bottom.png'):
            pyautogui.click(ev.point.x-50,ev.point.y+50)
            events.remove(ev)
        
        if(ev.name == 'learn_right_top.png'):
            pyautogui.click(ev.point.x+50,ev.point.y-50)
            events.remove(ev)

        if(ev.name == 'learn_left_top.png'):
            pyautogui.click(ev.point.x-50,ev.point.y-50)
            events.remove(ev)
        
            
    return(events)


def activation(img,main_arr):
    
    if (img.name == "main_task.png"):
        img.cond = False
        for i in main_arr:
            if (i.name == "new_task.png"):
                i.cond = True
            if (i.name == "go_to.png"):
                i.cond = True
            if (i.name == "go_to_foot.png"):
                i.cond = True
            if (i.name == "accept.png"):
                i.cond = True
            if (i.name == "compleat.png"):
                i.cond = True


    if (img.name == "go_to_foot.png"):
        img.cond = False
        for i in main_arr:
            if (i.name == "new_task.png"):
                i.cond = False
            if (i.name == "go_to.png"):
                i.cond = False

        
    if (img.name == "compleat.png"):
        for i in main_arr:
            if (i.name == "main_task.png"):
                i.cond = True
                
                
    if (img.name == "accept.png"):
        img.cond = False
        for i in main_arr:
            if (i.name == "new_task.png"):
                i.cond = True
            if (i.name == "go_to.png"):
                i.cond = True
            if (i.name == "go_to_foot.png"):
                i.cond = True
            if (i.name == "accept.png"):
                i.cond = True
            if (i.name == "compleat.png"):
                i.cond = True
        
    
    


def clicker(events):
    #print(events)
    for ev in events:
        #print(ev.name)
        pyautogui.click(ev.point.x+15,ev.point.y)

    


