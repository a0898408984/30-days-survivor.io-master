def maincost(lv=2):
    # lv > 1
    papers = [[1,3,1],[4,6,2],[7,9,3],[10,14,4],[15,19,5],[20,24,10],[25,29,15],[30,39,20],[40,49,25],[50,59,30],[60,64,50],[65,69,55],[70,74,60],[75,79,65],[80,84,70],[85,89,80],[90,94,90],[95,99,100],[100,104,120],[105,109,140]]
    money = [[i,i,i*1000] for i in range(1,10)] + [ [i*5,i*5+4,i*5000] for i in range(2,7)]\
        + [[35,39,40000],[40,49,50000],[50,59,75000],[60,64,100000],[65,69,150000],[70,74,200000],[75,79,250000],[80,84,250000],[85,89,350000],[90,94,400000],[95,99,500000],[100,104,700000],[105,109,700000] ]
    needspapers = 0
    needsmoney = 0
    for x in papers:
        for y in range(x[0],x[1]+1):
            if lv > y:
                needspapers+=x[2]
            else:
                break
    for x in money:
        for y in range(x[0],x[1]+1):
            if lv > y:
                needsmoney+=x[2]
            else:
                break
    return ([needspapers, needsmoney])

lvmapping = {i:maincost(i) for i in range(1, 101)}


# brutal force
def mainfunc(data = [[283,30,5],[253,50,7],[282,50,6]], money = 1502000, mode = 0):
    if mode == 1:
        money = 999999*1000
    tmpmax = [0,0,0]
    moneymax = 0
    for i in range(3):
        for j in range(1,101):
            if j > data[i][1]:
                tmpmax[i] = j-1
                moneymax += lvmapping[tmpmax[i]][1]
                break
            if data[i][0] < lvmapping[j][0]:
                tmpmax[i] = j-1
                moneymax += lvmapping[tmpmax[i]][1]
                break
    if moneymax <= money:
        return [tmpmax,moneymax,(tmpmax[0]-1)*data[0][2]+(tmpmax[1]-1)*data[1][2]+(tmpmax[2]-1)*data[2][2]]
    tmp = [1,1,1]
    tmpsel = [0,tmp]
    maxnum = -1
    for i in range(1, tmpmax[0]+1):
        for j in range(1, tmpmax[1]+1):
            for k in range(1, tmpmax[2]+1):
                if (i-1)*data[0][2]+(j-1)*data[1][2]+(k-1)*data[2][2]>= maxnum and\
                    lvmapping[i][1] + lvmapping[j][1] + lvmapping[k][1] <= money:
                    tmp = [i,j,k]
                    if (i-1)*data[0][2]+(j-1)*data[1][2]+(k-1)*data[2][2] == maxnum:
                        tmpsel.append([lvmapping[i][1] + lvmapping[j][1] + lvmapping[k][1], tmp])
                    else:
                        maxnum = (i-1)*data[0][2]+(j-1)*data[1][2]+(k-1)*data[2][2]
                        tmpsel = [[lvmapping[i][1] + lvmapping[j][1] + lvmapping[k][1], tmp]]
    tmpsel.sort()
    return [tmpsel[0][1],tmpsel[0][0],maxnum]
import datetime
def caltime(stamina, nextplus_minute):
    p = datetime.datetime.now()
    tmp = datetime.datetime(p.year,p.month,p.day,0,0,0) +  datetime.timedelta(days=1)
    if tmp-p < datetime.timedelta(minutes=+nextplus_minute):
        return stamina
    x = tmp-p+datetime.timedelta(minutes=-nextplus_minute)
    x = [int(y) for y in str(x).split('.')[0].split(':')]
    x = x[0] * 3600 + x[1] * 60 + x[2]
    return [x//1200 + 1 + stamina, x%1200, stamina, nextplus_minute]


武器上限等級 = 60
項鍊上限等級 = 60
手套上限等級 = 70
上衣上限等級 = 70
腰帶上限等級 = 50
鞋子上限等級 = 50


武器圖紙數量 = 730
項鍊圖紙數量 = 645
手套圖紙數量 = 758
上衣圖紙數量 = 751
腰帶圖紙數量 = 616
鞋子圖紙數量 = 694


武器增加數值 = 12
項鍊增加數值 = 9
手套增加數值 = 8
上衣增加數值 = 35
腰帶增加數值 = 23
鞋子增加數值 = 19

atk預算 = (1470+1245+1245)*1000 
hp預算 = (1470+1195+995)*1000


現在的體力 = 24
再多少分鐘增加一體力 = 9

ansatk = mainfunc([[武器圖紙數量,武器上限等級,武器增加數值],[項鍊圖紙數量,項鍊上限等級,項鍊增加數值],[手套圖紙數量,手套上限等級,手套增加數值]],atk預算)
anshp = mainfunc([[上衣圖紙數量,上衣上限等級,上衣增加數值],[腰帶圖紙數量,腰帶上限等級,腰帶增加數值],[鞋子圖紙數量,鞋子上限等級,鞋子增加數值]],hp預算)
ansstamina = caltime(現在的體力,再多少分鐘增加一體力)
print(ansatk, '-> atk')
print(anshp, '-> hp')
print(ansstamina[0], f'-> 午夜12點的體力值, 並經過時間{ansstamina[1]}秒({ansstamina[1]//60}分{ansstamina[1]%60}秒), 約差六十秒左右, in caltime({ansstamina[2]},{ansstamina[3]})')



  