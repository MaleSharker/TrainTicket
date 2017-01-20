#-*- coding:utf-8 -*-

import requests
# from bs4 import BeautifulSoup
# import code
import json
# from matplotlib.cbook import Null
from time import sleep
# from matplotlib.testing.compare import verify
# from test.test_codecs import UTF16BETest
import pygame
from _socket import timeout

url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-01-22&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=SJP&purpose_codes=ADULT"
targetTrains = ["Z202" ,"T370" ,"Z90" ,"K729" ,"K600" ,"Z14","T124","T254","Z236"]
n = 1

def playMusic():
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load('/Users/baichenchen/Desktop/sugar.mp3')
    pygame.mixer.music.play(0)
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy() & n > 0:
        pygame.event.poll()
        clock.tick(10)
    
def parseTicketJson(dicData):
    if len(dicData) < 10:
        return False
    try:
        jsonData = json.loads(dicData)
        status = jsonData["status"]
        if status == False :
            return False
        trainList = jsonData["data"]
        for dic in trainList:
            secTxt = dic["secretStr"]
            if len(secTxt) > 10:
                trainNum = dic["queryLeftNewDTO"]["station_train_code"]
                for num in targetTrains:
                    if trainNum == num:
                        print("train num - " + trainNum)
                        return True
    except:
        return False
    else:
        return False
    return False


while n > 0:
    try:
        req = requests.get(url,verify=False,timeout=5)
        isBook = parseTicketJson(req.content)
        if isBook:
            print("have ticket")
            playMusic()
            sleep(60)
        else:
            sleep(1)
#         pygame.mixer.stop()  
            print("time - 3")
    except:
        continue
    else:
        continue


