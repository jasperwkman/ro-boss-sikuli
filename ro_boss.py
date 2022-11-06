Settings.MoveMouseDelay=0
Settings.AutoWaitTimeout=1
Settings.ActionLogs=0
Settings.InfoLogs=0
from datetime import datetime as dt
import random
import myLib
reload(myLib)
from myLib import *
boss_list = myLib.boss_list
mylib=myLib()
myScriptPath="D:\\scripts\\ro_boss.sikuli"
if not myScriptPath in sys.path:sys.path.append(myScriptPath)
current_boss = ""
first_seq=["half-dragon","jirtas","hebamoo"]
second_seq = [x for x in mylib.boss_list.keys() if x not in first_seq ]
attack_sequence = first_seq + second_seq
fly_item=Location(1171, 808)
butterfly=Location(1278, 805)
attack=Location(1704, 800)
init_start = True
pre_visited = False

boss_round = 0
boss_icon_area=Region(471,219,144,123)

def close_game():
    if Region(1525,83,110,104).exists("boss_list_close_button.png"):
        click(Location(1576, 137))
        sleep(2)
    try:
        Region(316,43,37,42).click("1666743530236.png")
    except:
        mylib.popmsg("Cannot close game",1)

def open_game():

    while True:

        if Region(1663,874,86,95).exists("boss_list_button.png"):
            break
        
        sleep(5)

        if Region(1464,151,284,214).exists("1666656763700.png"):
            Region(1464,151,284,214).click("1666656763700.png")
            continue

        if Region(971,650,339,141).exists("1666772957869.png"):
            click(Location(1133, 718))
            sleep(5)
            continue
        
        if Region(832,689,293,133).exists("1666656829613.png") or Region(828,554,311,76).exists("1666656848572.png"):
            click(Location(924, 733))
            continue
        
        if Region(802,438,330,63).exists("1665663840947.png"):
            continue
        
        if Region(1377,821,333,145).exists("1666656885558.png"):
            popup("start game",1)
            click(Location(288, 282)) #choose 1st character
            sleep(2)
            click(Location(1525, 895))#click start game
            click(Location(1525, 895))#click start game
            continue
        
        if Region(634,816,283,104).exists("event_detail_button.png"):
            click(Location(1402, 178)) # click close event detail
            continue

        if Region(749,762,447,161).exists("1666005532823.png"):
            click(Location(946, 867)) # click close maintenance note
            continue

        if Region(168,84,1570,885).exists("1666265477505.png"):
            Region(168,84,1570,885).click("1666265477505.png")
            continue
        
#-----------------------------------------------------------
def handleException():
    mylib.popmsg("handleException",1)
#-----------------------------------------------------------
def check_boss_alive(boss, map_opened=False):
    m = None
    scrollDown = False
    if map_opened or mylib.open_mini_boss_list():
        if Region(282,159,176,810).exists(boss_list[boss]["list_icon"]):
            m = Region(282,159,176,810).find(boss_list[boss]["list_icon"])
        else: # if not found, scroll down and fin again
            dragDrop(Location(600, 800),Location(600, 300))
            scrollDown = True
            sleep(2)
            if Region(282,159,176,810).exists(boss_list[boss]["list_icon"]):
                m = Region(282,159,176,810).find(boss_list[boss]["list_icon"])
            else:
                mylib.popmsg("Boss " + boss + " not in the list.",1)
        if m != None:
            Region(281,194,151,765).click(boss_list[boss]["list_icon"])
        if m != None and Region(m.x +530 , m.y -20 ,160,110).exists("boss_show.png"):
            mylib.logmsg(boss + " exists")
            return True
        else:
            mylib.logmsg (boss + " is dead")
            if scrollDown:
                dragDrop(Location(600, 300),Location(600, 900))
                sleep(1)
                dragDrop(Location(600, 300),Location(600, 900))
                sleep(1.5)
            return False
    return False

#-----------------------------------------------------------
def go_to_boss():
    if mylib.open_mini_boss_list():
        if Region(1243,865,224,92).exists("1648895023027.png"):
            click(Location(1355, 908))
            return True
    return False

def pre_visit_boss():
    global pre_visited
    mylib.popmsg("pre-visit boss :" + boss,1)
    check_boss_alive(first_seq[0])
    go_to_boss()
    sleep(5)
    if Region(1525,83,110,104).exists("boss_list_close_button.png"):
        click(Location(1576, 137))
    wait_to_map()
    pre_visited = True
#-----------------------------------------------------------
def fly_and_atk_boss(boss):
    atk_icon = boss_list[boss]["atk_icon"]
    attacking = False
    i = 1
    fly_lock_check = False
    while i < 60:
        if attacking:
            mylib.popmsg("Missing boss :" + boss,1)
            if not check_boss_alive(boss): 
                # if is attacking, and already exist while bossIconArea.exists loop
                # means the boss may be dead or missing,
                # check the boss alive again.
                # if boss not alive, return Falase to quit function
                # if boss still alive, continus this loop to find boss again
                # if is not attacking, continue find boss
                if Region(1525,83,110,104).exists("boss_list_close_button.png"):
                    click(Location(1576, 137))
                return False
            
        if "mvp_icon" in boss_list[boss].keys():
            while boss_icon_area.exists(boss_list[boss]["mvp_icon"]):
                sleep (2)
        if boss_icon_area.exists(atk_icon):
            mylib.logmsg("Attacking boss :" + boss)
            attacking = True
            i = 1
            wait_attack(boss)
        else:
            attacking = False
            click(fly_item)
            if not fly_lock_check:
                if Region(628,372,672,362).exists("1666005385265.png"):
                    click(Location(855, 549))
                    click(Location(801, 676))
                    fly_lock_check = True
            i += 1
            if i == 30:
                if not check_boss_alive(boss):
                    return False
                else:
                    mylib.logmsg("Continue find boss :" + boss)
                if Region(1525,83,110,104).exists("boss_list_close_button.png"):
                    click(Location(1576, 137))
    return False
#-----------------------------------------------------------
def wait_to_map(boss):
    boss_map = boss_list[boss]["map"]
    for i in range(1,10):
        mylib.logmsg("waiting to " + boss + " boss map. #" + str(i))
        if mylib.open_big_map():
            if Region(1167,118,245,76).exists(boss_map):
                mylib.logmsg("arrived map")
                return True
            sleep(1)
    return False
#-----------------------------------------------------------
def wait_attack(boss):
    atk_icon = boss_list[boss]["atk_icon"]
    while (1):
        if boss_icon_area.exists(atk_icon):
            mylib.popmsg("Is attacking " + boss,1)
            if Region(1433,848,112,126).exists("1667036609066.png"):
                click(Location(1605, 926))
            sleep(3)
        else:
            break
        
#-----------------------------------------------------------
def is_attacking(boss):
    if current_boss == "":
        return False
    if bossIconArea.exists(boss_list[boss]["atk_icon"]):
        return true
    return False
            
#-----------------------------------------------------------
def pick_boss():
    global attack_sequence
    mylib.open_mini_boss_list()
    map_opened = True
    temp_sequence = attack_sequence[:]
    for boss in attack_sequence:
        if check_boss_alive(boss,map_opened):
            currentBoss = boss
            attack_sequence = temp_sequence[:]
            return boss
        else:
            mylib.logmsg("remove : " + boss)
            temp_sequence.remove(boss)
    currentBoss = ""
    return None

def back_to_city():
    if Region(1525,83,110,104).exists("boss_list_close_button.png"):
        click(Location(1576, 137))
        sleep(1)
    click(butterfly)
    sleep(5)
    try:
        Region(1663,874,86,95).wait("boss_list_button.png",20)
    except:
        mylib.logmsg("back to city")

#-----------------------------------------------------------
def change_job_for_boss(boss):
    job = mylib.job_icon[boss_list[boss]]
    if "1665896120521.png".exists(job["head"]):
        return True
    else:
        click(Location(1491, 806))
        sleep(1)
        click(job["book"])
        type(Key.ESC)
        
#-----------------------------------------------------------
def start_bossing():
    global pre_visited
    while (1):
        if is_attacking(current_boss):
            mylib.logmsg("Already attacking " + current_boss)
            wait_attack(current_boss)
            continue
        if not pre_visited:
            # if not pre-visited boss map, pick and find boss,
            # otherwise, skip and fly to attack boss
            boss = pick_boss() # pick a boss from boss list.
            if boss == None:
                break
            mylib.logmsg("Target boss #" + boss)
            # got to boss location, if can not get alive boss, exit
            if not go_to_boss():
                back_to_city()
                continue
            #change_job_for_boss(boss)
            if not wait_to_map(boss):
                back_to_city()
                continue
        
        if not fly_and_atk_boss(boss):
            mylib.popmsg("Can not find boss or boss is dead. Exit this loop.",1)
            pre_visited = False
            attack_sequence.remove(boss)
            back_to_city()
            continue

#-----------------------------------------------------------
def need_change_channel():
    ## To check if need to change to another channel. 
    ## after 5 round boss, having 25% chance to change another channel.
    ## and add 25% chance after each round.
    global boss_round
    
    if boss_round <= 5:
        return False
    ran = random.randint(1,4 - (boss_round - 4))
    if ran == 1:
        return True

def change_channel(num):
    mylib.popmsg("Change to channel #{}".format(str(num)),2)
    mylib.open_big_map()
    Region(1136,193,46,67).wait("1665735362943.png",5)
    Region(1136,193,46,67).click("1665735362943.png")
    Region(1389,185,235,241).wait("1665735501639.png",5)
    click(Location(1506, 306))
    sleep(1)
    type(str(num))
    sleep(1)
    click(Location(1682, 931))
    sleep(1)
    Region(1148,796,359,168).click("1665736245010.png")
    if Region(644,310,642,503).exists("1666005174249.png"):
        click(Location(853, 623))
        sleep(1)
        click(Location(1118, 748))

while True:
    global attack_sequence
    attack_sequence = first_seq + second_seq
    current_hour = dt.now().hour
    current_minute = dt.now().minute
    if ((current_hour >= 0 and current_minute > 10) and
       (current_hour <=4 and current_minute < 55)):
        #sleep between 00:10 and 4:55
        mylib.popmsg("Not in bossing hour.",1)
        sleep(59)
        continue
    ## if in boss hour go down

    sleep_sec = 30
    popup("current_minute: " + str(current_minute),1)
    if ((current_minute >= 25 and current_minute <=30) or 
        (current_minute >= 55 and current_minute <=59) or 
        current_minute == 0 or 
        init_start ):
        
        open_game()
        if not init_start:
            # if the script just start, skip waiting boss reborn,
            # go kill boss directly.
            while (1):
                min_now = dt.now().minute
                if  min_now in (26,27,28,56,57,58):
                    pre_visit_boss
                mylib.popmsg("Waiting boss reborn: "+ str(min_now),2)
                if min_now == 0 or min_now == 30:
                    break

        start_bossing()
        # double check all bosses are killed.
        mylib.popmsg("Double check bass cleared.",1)
        attack_sequence = first_seq + second_seq
        start_bossing()
        mylib.popmsg("Double check completed.",1)
        boss_round += 1
        if need_change_channel():
            change_channel(random.randint(1,30))
            boss_round = 0
            sleep_sec = (60*30)
        close_game()
    init_start = False
    
    mylib.popmsg(
        "Waiting next round for {} minutes . \n {} round after after previoos changing channel.".format(
            str(float(sleep_sec/60.0)),
            str(boss_round)
        ),1)
    sleep(sleep_sec)
    