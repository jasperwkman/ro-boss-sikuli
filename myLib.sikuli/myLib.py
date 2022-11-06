from sikuli.Sikuli import *
from datetime import datetime as dt

class myLib():

    lib_img_path = "myLib.sikuli/"
    job_icon = {
            "shadow":{ "head":lib_img_path+"1664864234705.png","book":Location(1264, 737)},
            "gun":{ "head":lib_img_path+"1665895544231.png","book":Location(1259, 650)}
            }
    boss_list = {
        "alice":{  
                "atk_icon":"1667027835332.png",
                "mvp_icon":"1666137996096.png",
                "list_icon":"alice_list_icon.png",
                "map":"alice_map.png",
                "job":"gun"
            },
        "jirtas":{
                "atk_icon":"jirtas_atk_icon.png",
                "list_icon":"jirtas_list_icon.png",
                "map":"jirtas_map.png",
                "job":"gun"
            },
        "dark-swordtest":{
                "atk_icon":"1666879539668.png",
                "list_icon":"dark-swordtest_list_icon.png",
                "map":"dark-swordtest_map.png",
                "job":"gun"
            },
        "hebamoo":{
                "atk_icon":"1666879447778.png",
                "list_icon":"hebamoo_list_icon.png",
                "map":"hebamoo_atk_map.png",
                "job":"gun"
            },
        "ice-statue":{
                "atk_icon":"1666879603984.png",
                "list_icon":"ice-statue_list_icon.png",
                "map":"ice-statue_map.png",
                "job":"gun"
            },
        "little-frame-witch":{
                "atk_icon":"1666877755287.png",
                "list_icon":"little-frame-witch_list_icon.png",
                "map":"little-frame-witch_map.png",
                "job":"gun"
            },
        "big-clock":{
                "atk_icon":"big-clock_atk_icon.png",
                "list_icon":"big-clock_list_icon.png",
                "map":"big-clock_map.png",
                "job":"shadow"
            },
        "half-dragon":{
                "atk_icon":"1666879358837.png",
                "mvp_icon":"1665907225006.png",
                "list_icon":"half-dragon_list_icon.png",
                "map":"half-dragon_map.png",
                "job":"gun"
            }
        }
    for k in boss_list.keys():
        boss_list[k]["atk_icon"] = lib_img_path + boss_list[k]["atk_icon"]
        boss_list[k]["list_icon"] = lib_img_path + boss_list[k]["list_icon"]
        boss_list[k]["map"] = lib_img_path + boss_list[k]["map"]

    
    bossListArea1 = Region(844,220,181,101)
    bossListArea2 = Region(864,353,164,96)
    bossListArea3 = Region(890,511,124,66)
    bossListArea4 = Region(891,640,134,87)
    bossListArea5 = Region(881,782,132,83)
    bossListClickPoint1 = Location(933, 269)
    bossListClickPoint2 = Location(923, 401)
    bossListClickPoint3 = Location(945, 538)
    bossListClickPoint4 = Location(941, 686)
    bossListClickPoint5 = Location(949, 820)

    attach_icon_area = Region(340,228,128,100)
    
    def popmsg(self,msg,sec=1):
        popup(msg,sec)
        self.logmsg(msg)
    
    def logmsg(self,msg):
        now = dt.now()
        print("{} -- {}".format(now.strftime("%d/%m/%Y %H:%M:%S"),msg))
        
    def open_mini_boss_list(self):
        for i in range(1,5):
            #try 5 times, if map opened, close it first
            if Region(1027,654,75,75).exists("word_icon.png"):
                click(Location(1681, 204))
                sleep(1)
                continue
        try:
            if not Region(1164,496,379,63).exists("1665223033014.png"):
                while Region(1465,143,79,27).exists("1665653605036.png"):
                    click(Location(1501, 155))#click more button
                    sleep(1)
                    if Region(1443,246,72,62).exists("1665653708874.png"):
                        click(Location(1472, 279))
                        sleep(1)
                        break
            # end if
            
            # if the mini boss list already show
            if Region(467,115,106,76).exists("1665223251804.png"):
                if Region(1071,414,162,75).exists("1665724628692.png"): #if return bank screen
                    if Region(1525,83,110,104).exists("boss_list_close_button-1.png"):
                        click(Location(1576, 137))
                    return open_mini_boss_list(self)
                else:
                    return True
            
            # if the mvp boss list on the screen
            if Region(482,122,80,61).exists("1648874529924.png"):
                Region(482,122,80,61).click("1648874529924.png") # click mini box
                if Region(1071,414,162,75).exists("1665724628692.png"): # if return bank screen
                    if Region(1525,83,110,104).exists("boss_list_close_button.png"):
                        click(Location(1576, 137))
                    return open_mini_boss_list(self)
                else:
                    return True
        except:
            popup("fail to open boss list",1)
        return False
    
    def open_big_map(self):
        if Region(1525,83,110,104).exists("1648894561690.png"): # if something opened, close it.
            click(Location(1576, 137))
        for i in range(1,61):
            if not Region(1027,654,75,75).exists("word_icon.png"):
                click(Location(1638, 212))
            else:
                return True
        return False

    def cancelAttack():
        if Region(1654,758,99,102).exists("1648880801237.png"):
            click(attack)