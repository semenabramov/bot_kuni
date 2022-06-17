import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
#from speedtest import Speedtest
#import telebot
#import psutil
import platform
#from PIL import Image

name = getpass.getuser()    # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())   # IP-адрес системы
mac = get_mac()   # MAC адрес
ost = platform.uname()  

print(name)
print(ip)
print(mac)
print(ost)