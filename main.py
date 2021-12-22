# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:13:18 2021

@author: Mad_ToBy
"""
import automate
from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import pandas as pd 
import time 
from datetime import datetime 

sym = 'BTCUSDT'
littleorderflag = 0#小时建仓信号
bigorderflag = 0#4小时建仓信号
i=0;
quantity = float(round(0.003, 3))
fifminsmacd = automate.macdindictator(sym,'15m')
hmacd = automate.macdindictator(sym,'1h')
fourhmacd = automate.macdindictator(sym,'4h')
littleorderflag = automate.signaloverturned(hmacd, fifminsmacd)
bigorderflag = automate.signaloverturned(fourhmacd,hmacd)
request_client = RequestClient(api_key="#")
postion = automate.postionorder(0,0,0,0,0,0,
                               0,0,0,0)


# this is the main package of automatetrade 
while True:
    #frist get the kline data and transfer to macd 
    try:
        oneminsmacd = automate.macdindictator(sym,'1m')
        if i%15 ==0:
            fifminsmacd = automate.macdindictator(sym,'15m')
        elif i%60==0:
            hmacd = automate.macdindictator(sym,'1h')
            littleorderflag = automate.signaloverturned(hmacd, fifminsmacd)
        elif i%240 == 0:
            fourmacd = automate.macdindictator(sym,'4h')
            bigorderflag = automate.signaloverturned(fourhmacd,hmacd)
    except Exception  as er : 
        timestamp = datetime.now()
        timestamp = datetime.timestamp(timestamp)
        error = str (er)
        error.rstrip()
        error.rstrip()
        error.lstrip()
        action = 'something happend \n'+error
        automate.record(action,timestamp)
   
    if littleorderflag != 0 and oneminsmacd.iloc[-2] * oneminsmacd.iloc[-1] <0 and littleorderflag *oneminsmacd.iloc[-1]>0: 
        result = request_client.get_mark_price(symbol="BTCUSDT")
        price = float(round(result.markPrice,0))
        tempflag = littleorderflag
        automate.post_order(tempflag,price,quantity,500)
        automate.remind()
        #time.sleep(1800)
        #i =i +30
        try:
            pass
             #automate.closewrongpostion(fifminsmacd,tempflag)
        except Exception:
            pass
        littleorderflag = 0
    if bigorderflag != 0 and oneminsmacd.iloc[-2] * oneminsmacd.iloc[-1] <0 and bigorderflag *fifminsmacd.iloc[-1]>0:
        result = request_client.get_mark_price(symbol="BTCUSDT")
        price = float(round(result.markPrice,0))
        tempflag = bigorderflag
        automate.post_order(tempflag,price,quantity,1000)
        automate.remind()        
        #time.sleep(7200)
        #i = i +120
        try:
            pass 
           #automate.closewrongpostion(fifminsmacd,tempflag)
        except Exception:
            pass
        bigorderflag = 0
    time.sleep(60)
    i=i+1;
    ##啊需要一个大的趋势检测 还要一个平仓策略 大概就是两个小时后如果MACD回缩，就平仓，然后如果没有就MACD归0平仓 以及建仓提醒 ，还有如何应对短暂下降然后相应呢？
    ##目前來説沒有什麽需要改進的東西了，可以等等試試檢測震蕩趨勢的可能
    ##太他妈弱智了，我说怎么会买入，他妈的由于一直没有满足后面几个条件，导致一直没有购买，然后flag一直没有置零，结果后面12个小时又买入卧槽。
    
