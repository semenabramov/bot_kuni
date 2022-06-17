from numpy import array
import get_loc_pic as pic
import pyautogui
from time import sleep
from classes import *
import os

#def import_images(directory):
#    files = os.listdir(directory)
#    pic_arr = []
#    for name in files:
#        pic_arr.append(Image(name,0.7))
#    return pic_arr

pic_arr = []
pic_arr.append(Image("arrow.png",0.6,0.1))
pic_arr.append(Image("up.png",0.7,30))
pic_arr.append(Image("zadanie.png",0.7,90))

pic_arr.append(Image("learn_left_bottom.png",0.7,7))
pic_arr.append(Image("learn_left_top.png",0.7,7))
pic_arr.append(Image("learn_right_bottom.png",0.7,7))
pic_arr.append(Image("learn_right_top.png",0.7,7))
pic_arr.append(Image("x.png",0.7,5,False))
pic_arr.append(Image("toch.png",0.7,5,False))
pic_arr.append(Image("scroll.png",0.7,5,False))


pic_arr.append(Image("main_task.png",0.6,7))
pic_arr.append(Image("new_task.png",0.7,3,False))
pic_arr.append(Image("go_to.png",0.7,3,False))
pic_arr.append(Image("go_to_foot.png",0.75,3,False))
    
    
pic_arr.append(Image("compleat.png",0.7,15,False))
pic_arr.append(Image("accept.png",0.7,15,False))
    

while 1:
    #sleep(0.1)
    #print('*')
    
    res = pic.find(pic_arr)
    res = pic.filter(res)
    pic.clicker(res)
    
#pic_arr = import_images('../image')