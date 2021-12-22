# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:26:23 2021

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
import schedule

sym = 'BTCUSDT'

bigorderflag = 0#4小时建仓信号
quantity = float(round(0.003, 3))
fifminsmacd = automate.macdindictator(sym,'15m')
hmacd = automate.macdindictator(sym,'1h')
fourhmacd = automate.macdindictator(sym,'4h')
bigorderflag = automate.signaloverturned(fourhmacd,hmacd)
request_client = RequestClient("#")
oneminsmacd = automate.macdindictator(sym,'1m')
hourbbol = automate.bollindicator(sym,'1h')
fourhourbbol =automate.bollindicator(sym,'4h')
postionlist =[automate.postionorder(0,0,0,0,0,0,0,0,0,0)]

# this is the main package of automatetrade 
def minlytrade():
    global littleorderflag, oneminsmacd,bigorderflag,fifminsmacd,hourbbol,fourhourbbol,postionlist
    #frist get the kline data and transfer to macd 
    #try:
    try:
        oneminsmacd = automate.macdindictator(sym,'1m')
    except :
        pass
    i = 0
    for i in range(len(postionlist)): 
        result = postionlist[i].check(postionlist)
        if result:
            postionlist.remove(postionlist[i])
    #except Exception  as er : 
        ''' timestamp = datetime.now()
        timestamp = datetime.timestamp(timestamp)
        error = str (er)
        error.rstrip()
        error.rstrip()
        error.lstrip()
        action = 'something happend \n'+error
        automate.record(action,timestamp)
        '''
    if bigorderflag != 0  and bigorderflag *fifminsmacd.iloc[-1]>0 and bigorderflag *oneminsmacd.iloc[-2]>0 and len(postionlist) == 1 :
        result = request_client.get_mark_price(symbol="BTCUSDT")
        price = float(round(result.markPrice,0))
        tempflag = bigorderflag
        result = automate.post_order(tempflag,price,quantity,600,fourhourbbol)
        if result !=0:
            postionlist.append(result)
        automate.remind()        
            #time.sleep(7200)
            #i = i +120          
        bigorderflag = 0
        
    
def fifminlytrade():
    global fifminsmacd
    try:
        fifminsmacd = automate.macdindictator(sym,'15m')
    except Exception  as er : 
        timestamp = datetime.now()
        timestamp = datetime.timestamp(timestamp)
        error = str (er)
        error.rstrip()
        error.rstrip()
        error.lstrip()
        action = 'something happend \n'+error
        automate.record(action,timestamp)
        
def hourlytrade():
    global hmacd,littleorderflag,fifminsmacd,postionlist,hourbool
    #try:
    hmacd = automate.macdindictator(sym,'1h')
    for i in range(len(postionlist)): 
        result = postionlist[i].upgrade()
        ''' except Exception  as er : 
        timestamp = datetime.now()
        timestamp = datetime.timestamp(timestamp)
        error = str (er)
        error.rstrip()
        error.rstrip()
        error.lstrip()
        action = 'something happend \n'+error
        automate.record(action,timestamp)
        '''
    hourbbol = automate.bollindicator(sym,'1h')
    
    
    
    
def fourhourlytrade():
    global fourhmacd,bigorderflag,hmacd,fourhourbbol
    try:
        fourhmacd = automate.macdindictator(sym,'4h')
    except Exception  as er : 
        timestamp = datetime.now()
        timestamp = datetime.timestamp(timestamp)
        error = str (er)
        error.rstrip()
        error.rstrip()
        error.lstrip()
        action = 'something happend \n'+error
        automate.record(action,timestamp)
    bigorderflag = automate.signaloverturned(fourhmacd,hmacd)
    fourhourbbol =automate.bollindicator(sym,'4h')

schedule.every(1).minutes.do(minlytrade)
schedule.every(7.5).minutes.do(fifminlytrade)
schedule.every(30).minutes.do(hourlytrade)
schedule.every(2).hours.do(fourhourlytrade)

while True:
    schedule.run_pending()
    time.sleep(1)