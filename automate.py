# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 22:46:51 2021

@author: Mad_ToBy
"""

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *
import pandas as pd 
import btalib
import time 
from datetime import datetime

class postionorder():
    def __init__(self,orderid,ordertype,slid,tpid,interval, bbol,X,price,quantity,number):
        self.orderid = orderid
        self.ordertype = ordertype 
        self.slid = slid 
        self.tpid =tpid 
        self.number = number
        self.interval = interval
        self.bbol = bbol
        self.X = X
        self.price = price
        self.quantity = quantity
        
    def upgrade(self):
        if self.orderid == 0 or self.tpid == 0 or self.slid ==0:
            return 0
        request_client = RequestClient(api_key='iCbttLmZY0donN6Intz6ugDzClWvjXYymfgmFtgVL42oC0yAdfzksLpPnoHkDLwJ', secret_key='eo8auIjXwXXpxjqrVl6yu6l0dOOyjAt113VzHEPLllwQBrN9kizE4ZL8OKisbQcJ')
        #result = request_client.cancel_order(symbol="BTCUSDT", orderId=self.tpid)
        #result = request_client.cancel_order(symbol="BTCUSDT", orderId=self.slid)
        self.bbol = bollindicator('BTCUSDT',self.number)
        '''if self.ordertype == 1:#buy
                                    try:
                                        if self.X == 'top':
                                            """take profit  everytime"""
                                            tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, 
                                                                           ordertype=OrderType.TAKE_PROFIT, price =round(self.bbol.top[-1]+self.interval), quantity = self.quantity,stopPrice=round(self.bbol.top[-1]+self.interval) ,reduceOnly=True,positionSide="BOTH")
                                            "and the stop loss"
                                            slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, 
                                                                           ordertcype=OrderType.STOP, stopPrice=round(self.bbol.mid[-1]), price =round(self.bbol.mid[-1]),reduceOnly = True,quantity=self.quantity,positionSide="BOTH")
                                            self.slid = slresult.orderId
                                            self.tpid = tpresult.orderId
                                        elif self.X == 'mid' :#and self.price < self.bbol.mid[-1]:
                                            tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.TAKE_PROFIT, price =round(self.bbol.top[-1]), stopPrice=round(self.bbol.top[-1]),
                                                                           quantity = self.quantity,reduceOnly=True,positionSide="BOTH")
                                            slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, stopPrice=round(self.bbol.bot[-1]),
                                                                           price =round(self.bbol.bot[-1]),reduceOnly = True,quantity=self.quantity,positionSide="BOTH")
                                            self.slid = slresult.orderId
                                            self.tpid = tpresult.orderId
                                        #elif self.X == 'mid' and self.price > self.bbol.mid[-1]:
                                            #tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.TAKE_PROFIT, price =round(bbol.top[-1]), stopPrice=round(bbol.top[-1]),
                                              #                             quantity = self.quantity,reduceOnly=True,positionSide="BOTH")
                                            #slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, stopPrice=round(bbol.mid[-1]),
                                             #                              price =round(bbol.mid[-1]),reduceOnly = True,quantity=self.quantity,positionSide="BOTH")
                                                                                 
                                        elif self.X =='bot':
                                           tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.TAKE_PROFIT, price =round(self.bbol.mid[-1]), stopPrice=round(self.bbol.mid[-1]) ,reduceOnly=True,quantity=self.quantity,positionSide="BOTH")
                                           slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertcype=OrderType.STOP, stopPrice=float(round(self.bbol.bot[-1]-self.interval)), price =float(round(self.bbol.bot[-1]-self.interval)),reduceOnly = True,
                                                                           quantity=self.quantity,positionSide="BOTH")
                                           self.slid = slresult.orderId
                                           self.tpid = tpresult.orderId
                                    except Exception :
                                       pass
                                    
                                if self.ordertype == -1:#sell 
                                    try:
                                        """take profit everytime"""
                                        if self.X == 'top':
                                            tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                                                       stopPrice=round(self.bbol.mid[-1]),price = round(self.bbol.mid[-1]),reduceOnly=True,quantity = self.quantity,positionSide="BOTH")
                                            "and the stop loss"
                                            slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                                                       stopPrice=float(round(self.bbol.top[-1]+self.interval)),price = float(round(self.bbol.top[-1]+self.interval)),quantity=self.quantity,positionSide="BOTH")
                                            self.slid = slresult.orderId
                                            self.tpid = tpresult.orderId
                                        if self.X =='mid':#and self.price <self.bbol.mid[-1]:
                                            tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                                                       stopPrice=round(self.bbol.bot[-1]),price = round(self.bbol.bot[-1]),reduceOnly=True,quantity = self.quantity,positionSide="BOTH")
                                            slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                                                       stopPrice=round(self.bbol.mid[-1]),price =round( self.bbol.mid[-1]),quantity=self.quantity,positionSide="BOTH")
                                            self.slid = slresult.orderId
                                            self.tpid = tpresult.orderId
                                        if self.X == 'bot':
                                            tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                                                       stopPrice=float(round(self.bbol.bot[-1]-self.interval)),price =float(round(self.bbol.bot[-1]-self.interval)),reduceOnly=True,quantity = self.quantity,positionSide="BOTH")
                                            slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                                                       stopPrice=round(self.bbol.mid[-1]),price = round(self.bbol.mid[-1]),quantity=self.quantity,positionSide="BOTH")
                                            self.slid = slresult.orderId
                                            self.tpid = tpresult.orderId
                                    except Exception as er:
                                      pass
                                elif self.ordertype == 0:
                                    pass'''
    def check(self,postionlist):
        request_client = RequestClient(api_key='iCbttLmZY0donN6Intz6ugDzClWvjXYymfgmFtgVL42oC0yAdfzksLpPnoHkDLwJ', secret_key='eo8auIjXwXXpxjqrVl6yu6l0dOOyjAt113VzHEPLllwQBrN9kizE4ZL8OKisbQcJ')
        result = request_client.get_position_v2()
        for i in result:
            if i.symbol =='BTCUSDT':
                btc = i.entryPrice
                
        if len(postionlist) == 2 and btc == 0:
            try:
                request_client.cancel_order(symbol = 'BTCUSDT',orderId = self.tpid)
                request_client.cancel_order(symbol = 'BTCUSDT',orderId = self.slid)
            except Exception as er:
                pass
            
            return 1
        
        if self.orderid == 0 :
            return 0
        slresult = request_client.get_order(symbol="BTCUSDT", orderId=self.slid)
        tpresult = request_client.get_order(symbol='BTCUSDT',orderId=self.tpid)
        self.price = round(request_client.get_mark_price('BTCUSDT').markPrice)
        if slresult.status =='EXPIRED'or slresult.status == 'CANCELLED':
            request_client.cancel_order(symbol = 'BTCUSDT',orderId = self.tpid)
            return 1
        elif tpresult.status =='EXPIRED' or tpresult.status =='CANCELLED':
            request_client.cancel_order(symbol = 'BTCUSDT',orderId = self.slid)
            return 1 
        else:
            pass
            
    
        



def post_order(orderflag,price,quantity,interval,bbol):
    top = abs(bbol.top[-1] - price)
    bot = abs(bbol.bot[-1] - price)
    mid = abs(bbol.mid[-1] - price)
    X = 'mid' if mid <bot and mid <top else 'top' if top < bot and top<mid else 'bot'
    request_client = RequestClient(api_key='iCbttLmZY0donN6Intz6ugDzClWvjXYymfgmFtgVL42oC0yAdfzksLpPnoHkDLwJ', secret_key='eo8auIjXwXXpxjqrVl6yu6l0dOOyjAt113VzHEPLllwQBrN9kizE4ZL8OKisbQcJ')
    if orderflag == 1:#buy
        try:
            timestamp = datetime.now()
            timestamp = datetime.timestamp(timestamp)
            result = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.MARKET, quantity=quantity, positionSide="BOTH")
            if X == 'top'and price < bbol.top[-1]:
                """take profit 500point everytime"""
                tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, 
                                                   ordertype=OrderType.TAKE_PROFIT, price =round(bbol.top[-1]+interval), quantity = quantity,stopPrice=float(round(bbol.top[-1]+interval)) ,reduceOnly=True,positionSide="BOTH")
                "and the stop loss"
                slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, 
                                                   ordertcype=OrderType.STOP, stopPrice=round(bbol.bot[-1]), price =round(bbol.bot[-1]),reduceOnly = True,quantity=quantity,positionSide="BOTH")
                number = '1h' if interval == 500 else '4h'
                postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
                return postion
            if X == 'top'and price > bbol.top[-1]:
                tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, 
                                                   ordertype=OrderType.TAKE_PROFIT, price =round(price+interval), quantity = quantity,stopPrice=float(round(price+interval)) ,reduceOnly=True,positionSide="BOTH")
                "and the stop loss"
                slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, 
                                                   ordertcype=OrderType.STOP, stopPrice=round(bbol.bot[-1]), price =round(bbol.bot[-1]),reduceOnly = True,quantity=quantity,positionSide="BOTH")
                number = '1h' if interval == 500 else '4h'
                postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
                return postion
            elif X == 'mid':#and price<bbol.mid[-1]:
               tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.TAKE_PROFIT, price =round(bbol.top[-1]), stopPrice=round(bbol.top[-1]),
                                                   quantity = quantity,reduceOnly=True,positionSide="BOTH")
               slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, stopPrice=round(bbol.bot[-1]),
                                                   price =round(bbol.bot[-1]),reduceOnly = True,quantity=quantity,positionSide="BOTH")
               number = '1h' if interval == 500 else '4h'
               postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
               return postion 
            
            #elif X == 'mid'and price>bbol.mid[-1]:
                 #tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.TAKE_PROFIT, price =round(bbol.top[-1]), stopPrice=round(bbol.top[-1]),
                                                   #quantity = quantity,reduceOnly=True,positionSide="BOTH")
                 #slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.STOP, stopPrice=round(bbol.mid[-1]),
                                                   #price =round(bbol.mid[-1]),reduceOnly = True,quantity=quantity,positionSide="BOTH")
            elif X =='bot':
                tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.TAKE_PROFIT, price =round(bbol.mid[-1]), stopPrice=round(bbol.mid[-1]) ,reduceOnly=True,quantity=quantity,positionSide="BOTH")
                slresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertcype=OrderType.STOP, stopPrice=round(bbol.bot[-1]-interval), price =round(bbol.bot[-1]-interval),reduceOnly = True,
                                                   quantity=quantity,positionSide="BOTH")
                number = '1h' if interval == 500 else '4h'
                postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
                return postion
            action = 'open a buyer postion with quantity 0.03 at'+ str(price) + 'with internl' +str(interval)
            record(action,timestamp)
        except Exception as er:
            error = str(er)
            error.rstrip()
            error.lstrip()
            error.rstrip()
            action = 'something happend'+error
            record(action,timestamp)
            return 0 
        else:
            record('done',timestamp)
    if orderflag == -1:#sell 
        X = 'mid' if mid <bot and mid <top else 'top' if top < bot and top<mid else 'bot'
        try:
            timestamp = datetime.now()
            timestamp = datetime.timestamp(timestamp)
            result = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.MARKET, quantity=quantity, positionSide="BOTH")
            """take profit 500point everytime"""
            if X == 'top':
                tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                               stopPrice=round(bbol.bot[-1]),price = round(bbol.bot[-1]),reduceOnly=True,quantity = quantity,positionSide="BOTH")
                "and the stop loss"
                slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                               stopPrice=round(bbol.top[-1] + interval),price =round(bbol.top[-1]+interval),quantity=quantity,positionSide="BOTH")
                number = '1h' if interval == 500 else '4h'
                postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity)
                return postion
            #if X ==' mid'and price < bbol.mid[-1]:
                
                #tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                               #stopPrice=round(bbol.bot[-1]),price = round(bbol.bot[-1]),reduceOnly=True,quantity = quantity,positionSide="BOTH")
                #slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                               #stopPrice=round(bbol.mid[-1]),price = round(bbol.mid[-1]),quantity=quantity,positionSide="BOTH")
            if X =='mid':#and price > bbol.mid[-1]:
                 tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                               stopPrice=round(bbol.bot[-1]),price = round(bbol.bot[-1]),reduceOnly=True,quantity = quantity,positionSide="BOTH")
                 slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                   stopPrice=round(bbol.top[-1]),price = round(bbol.top[-1]),quantity=quantity,positionSide="BOTH")
                 number = '1h' if interval == 500 else '4h'
                 postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
                 return postion
            if X == 'bot'and price >bbol.bot[-1]:
                tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                               stopPrice=round(bbol.bot[-1] - interval),price =round(bbol.bot[-1] - interval),reduceOnly=True,quantity = quantity,positionSide="BOTH")
                slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                               stopPrice=round(bbol.mid[-1]),price = round(bbol.mid[-1]),quantity=quantity,positionSide="BOTH") 
                number = '1h' if interval == 500 else '4h'
                postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
                return postion
            if X == 'bot'and price < bbol.bot[-1]:
                tpresult = request_client.post_order(symbol="BTCUSDT", side=OrderSide.BUY, ordertype=OrderType.TAKE_PROFIT,
                                               stopPrice=round(price - interval),price =round(price - interval),reduceOnly=True,quantity = quantity,positionSide="BOTH")
                slresult = request_client.post_order(symbol="BTCUSDT", reduceOnly=True, side=OrderSide.BUY, ordertype=OrderType.STOP, 
                                               stopPrice=round(bbol.mid[-1]),price = round(bbol.mid[-1]),quantity=quantity,positionSide="BOTH") 
                number = '1h' if interval == 500 else '4h'
                postion = postionorder(result.orderId,orderflag,slresult.orderId,tpresult.orderId,interval,bbol,X,price,quantity,number)
                return postion    
            action = 'open a SELLER postion with quantity 0.03 at'+ str(price) + 'with internl' +str(interval)
            record(action,timestamp)
        except Exception as er:
            error = str(er)
            error.rstrip()
            error.lstrip()
            error.rstrip()

            action = 'something happend'+error
            record(action,timestamp)
            return 0
        else:
            record('done',timestamp)
def signaloverturned(macd1,macd2):
    # calculate
    if  macd1[-1]*macd1[-2]<0 and macd2[-1]*macd1[-1] >0 :
        if macd1[-1]<0:
            flag = -1
        else:
            flag = 1
        if checkincrese(macd2,flag):     
            return flag 
        else:
            return 0
    return 0 
def macdindictator(sym,interval):
    client = RequestClient(api_key='iCbttLmZY0donN6Intz6ugDzClWvjXYymfgmFtgVL42oC0yAdfzksLpPnoHkDLwJ', secret_key='eo8auIjXwXXpxjqrVl6yu6l0dOOyjAt113VzHEPLllwQBrN9kizE4ZL8OKisbQcJ')
    
    try:data = client.get_candlestick_data(sym, interval,limit = 100 )
    except Exception as ER:
        pass
    truedata  = []
    client_columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume',
              'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore']
    for i in data :
        truedata.append([i.openTime,i.open,i.high,i.low,i.close,i.volume,i.closeTime,i.quoteAssetVolume,i.numTrades,i.takerBuyBaseAssetVolume,i.takerBuyQuoteAssetVolume,i.ignore])
        data2 = pd.DataFrame(truedata, columns=client_columns)
    data2['timestamp'] = pd.to_timedelta(data2['timestamp'])
    data2.set_index('timestamp', inplace=True)

    # validate data types for ohlcv columns
    ohlcv_columns = ['open', 'high', 'low', 'close', 'volume']
    data2[ohlcv_columns] = data2[ohlcv_columns].astype('float')
    btalib_macd = btalib.macd(data2, pfast=12, pslow=26, psignal=9).df
    return btalib_macd.histogram

def bollindicator(sym,interval):
    client = RequestClient(api_key='iCbttLmZY0donN6Intz6ugDzClWvjXYymfgmFtgVL42oC0yAdfzksLpPnoHkDLwJ', secret_key='eo8auIjXwXXpxjqrVl6yu6l0dOOyjAt113VzHEPLllwQBrN9kizE4ZL8OKisbQcJ')
    data = client.get_candlestick_data(sym, interval,limit = 100 )
    truedata  = []
    client_columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume',
              'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore']
    for i in data :
        truedata.append([i.openTime,i.open,i.high,i.low,i.close,i.volume,i.closeTime,i.quoteAssetVolume,i.numTrades,i.takerBuyBaseAssetVolume,i.takerBuyQuoteAssetVolume,i.ignore])
        data2 = pd.DataFrame(truedata, columns=client_columns)
    data2['timestamp'] = pd.to_timedelta(data2['timestamp'])
    data2.set_index('timestamp', inplace=True)
    # validate data types for ohlcv columns
    ohlcv_columns = ['open', 'high', 'low', 'close', 'volume']
    data2[ohlcv_columns] = data2[ohlcv_columns].astype('float')
    btalib_boll = btalib.bbands(data2)
    return btalib_boll.df

def checkincrese(macd1,orderflag):
    return True
    ''' if abs(macd1[-1])>abs(macd1[-2]) and macd1[-1]*orderflag >0:
        return 1 
    else:
        return 0
    '''

def closewrongpostion(macd,orderflag):
    #看15分线，倘若1"5分线在开仓后两根线都"收缩，平仓
    client = RequestClient(api_key='iCbttLmZY0donN6Intz6ugDzClWvjXYymfgmFtgVL42oC0yAdfzksLpPnoHkDLwJ', secret_key='eo8auIjXwXXpxjqrVl6yu6l0dOOyjAt113VzHEPLllwQBrN9kizE4ZL8OKisbQcJ')
    marketprice = client.get_mark_price('BTCUSDT').markPrice
    if checkincrese(macd,orderflag) != True:
        result  = client.cancel_all_orders(symbol='BTCUSDT')
        result = post_order(orderflag, float(round(markprice)),0.003,500)
        automate_func.remind()
    return 
def remind():
    #Beep(500,600)
    
    
    pass
def record(action,timestamp = 000000000):
    f = open('log.text','a')
    dt_object = datetime.fromtimestamp(timestamp)
    f.write(action+' at '+str(dt_object)+'\n')
    f.close()
    


