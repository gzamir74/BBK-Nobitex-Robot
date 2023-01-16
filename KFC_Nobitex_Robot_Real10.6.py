EndPoint="api.nobitex.ir"
#EndPoint="testnetapi.nobitex.ir"

def tick():
    global TradeAllowed
    global order_price
    if(dst.get().lower()=="usdt"): 
        symb1=src.get()+"USDT"
    else: 
        symb1=src.get()+"IRT"
        
    window.title(str(Username)+" : "+unixstamp2date(int(time.time()))+'  - KFC Nobitex Robot 10.6')
    ###################################################
    global layer
    global Lastid
    ka=0.1
    kb=0.2
    kc=0.2
    p=get_lastprice2(symb1.upper())#change all to uppercase to avoid error
    try:
        r2=VR2.get()
        r1=VR1.get()
        s1=VS1.get()
        s2=VS2.get()
        
        r3r2=VR3.get()-VR2.get()
        r2r1=VR2.get()-VR1.get()
        r1s1=VR1.get()-VS1.get()
        s1s2=VS1.get()-VS2.get()
        s2s3=VS2.get()-VS3.get()
    except Exception as e:
        messagebox.showerror(
            title='set values',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e)+"\n" #e is a class so used str
        )
        VR2.set(0)
        VR1.set(0)
        VS1.set(0)
        VS2.set(0)
        VR3.set(0)
        VS3.set(0)
        r2=VR2.get()
        r1=VR1.get()
        s1=VS1.get()
        s2=VS2.get()
        
        r3r2=VR3.get()-VR2.get()
        r2r1=VR2.get()-VR1.get()
        r1s1=VR1.get()-VS1.get()
        s1s2=VS1.get()-VS2.get()
        s2s3=VS2.get()-VS3.get()
     
    ######################
    #open buy scenarios
    ######################
    if(layer=="None" and p>s2+ka*s1s2 and p<s2+kb*s1s2 and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")
        print("Condition : buy at S2",order_price," , ",s2+ka*s1s2," , ",s2+kb*s1s2)
        res=RunBuy()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="S2"
                print("buy opened at S2 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("buy opened at S2 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("buy at S2 : Canceled")
                print("-------------------------------------------------")                
                break
            
                
    if(layer=="None" and p>s1+ka*r1s1 and p<s1+kb*r1s1 and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")
        print("Condition : buy at S1",order_price," , ",s1+ka*r1s1," , ",s1+kb*r1s1)
        res=RunBuy()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="S1"
                print("buy opened at S1 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("buy opened at S1 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("buy at S1 : Canceled")
                print("-------------------------------------------------")                
                break
            
    if(layer=="None" and p>r2+ka*r3r2 and p<r2+kb*r3r2 and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")        
        print("Condition : buy at R2",order_price," , ",r2+ka*r3r2," , ",r2+kb*r3r2)
        res=RunBuy()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="R2"
                print("buy opened at R2 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("buy opened at R2 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("buy at R2 : Canceled")
                print("-------------------------------------------------")                
                break
    
    if(layer=="None" and p>r1+ka*r2r1 and p<r1+kb*r2r1 and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")        
        print("Condition : buy at R1",order_price," , ",r1+ka*r2r1," , ",r1+kb*r2r1)
        res=RunBuy()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="R1"
                print("buy opened at R1 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("buy opened at R1 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("buy at R1 : Canceled")
                print("-------------------------------------------------")                
                break

    ######################
    #sell scenarios(after buy)
    ######################

    if(layer=="S2" and (p>s1-kc*s1s2 or p<s2-kc*s2s3) and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")        
        print("Condition : sell at S2",order_price," , ",s1-kc*s1s2," , ",s2-kc*s2s3)
        res=RunSell()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="None"
                print("sell  at S2 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("sell  at S2 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("sell at S2 : Canceled")
                print("-------------------------------------------------")                
                break
            
    if(layer=="S1" and (p>r1-kc*r1s1 or p<s1-kc*s1s2) and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")        
        print("Condition : sell at S1",order_price," , ",r1-kc*r1s1," , ",s1-kc*s1s2)
        res=RunSell()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="None"
                print("sell  at S1 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("sell  at S1 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("sell at S1 : Canceled")
                print("-------------------------------------------------")                
                break
            
    if(layer=="R2" and (p>r3-kc*r3r2 or p<r2-kc*r2r1) and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")
        print("Condition : sell at R2",order_price," , ",r3-kc*r3r2," , ",p<r2-kc*r2r1)
        res=RunSell()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="None"
                print("sell  at R2 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("sell  at R2 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("sell at R2 : Canceled")
                print("-------------------------------------------------")                
                break
   
    if(layer=="R1" and (p>r2-kc*r2r1 or p<r1-kc*r1s1) and TradeAllowed):
        order_price=str(p)
        print("-------------------------------------------------")        
        print("Condition : sell at R1",order_price," , ",r2-kc*r2r1," , ",r1-kc*r1s1)
        res=RunSell()
        while(True):
            ss=get_order_status(Lastid)
            if(ss=="Done"):
                layer="None"
                print("sell  at R1 : Done")
                get_order_detail(Lastid)
                print("-------------------------------------------------")                
                break
            if(ss=="Failed"):
                print("sell  at R1 : Failed")
                print("-------------------------------------------------")                
                break
            if(ss=="Canceled"):
                layer="None"
                print("sell at R1 : Canceled")
                print("-------------------------------------------------")                
                break
            
##    ########################################################        
##    #check order status for next action        
##    if(Lastid !="None" and get_order_status(Lastid)=="Done"):
##        TradeAllowed=False
##    else:
##        TradeAllowed=True
##    ########################################################
    time_string = "Price : "+str(p).ljust(12, ' ')+" Traded Level : "+layer#+"\n"+str(ss2).ljust(20, ' ')
    clock.config(text=time_string)
    clock.after(15000, tick)

def RunBuy():
    global TradeAllowed
    if(TradeAllowed):
        print("Try to buy at best market price")
        global myToken
        global Lastid
        Lastid="None"
        if(float(entry_Vamount.get()) <=0):
            messagebox.showerror(
                title='Buy status',
                message="Enter amount Correctly"
            )
            
            am=eg.enterbox(msg="Enter amount")
            if(am != None):
                Vamount.set(am)
            return("Failed")
        try:
            a=Buy_Market(src.get(),dst.get(),entry_Vamount.get(),order_price,"",myToken,EndPoint)
            idu=str(a["order"]["id"])
            stat=str(a["order"]["status"])
            print("id=",idu)
            Lastid=idu
            #rr=get_order_status(idu)
            return(stat)
        except Exception as e:
            messagebox.showerror(
                title='Buy status',
                message="Something is wrong\n"+e.__class__.__name__+": "+str(e)+"\n"+a["message"] #e is a class so used str
            )
            return("Failed")
    
def RunSell():
    global TradeAllowed
    if(TradeAllowed):
        print("Try to sell at best market price")
        global myToken
        global Lastid
        Lastid="None"
        if(float(entry_Vamount.get()) <=0):
            messagebox.showerror(
                title='Buy status',
                message="Enter amount Correctly"
            )
            
            am=eg.enterbox(msg="Enter amount")
            if(am != None):
                Vamount.set(am)
            return("Failed")
        try:
            a=Sell_Market(src.get(),dst.get(),entry_Vamount.get(),order_price,"",myToken,EndPoint)
            idu=str(a["order"]["id"])
            stat=str(a["order"]["status"])
            print("id=",idu)
            Lastid=idu
            #rr=get_order_status(idu)
            return(stat)
        except Exception as e:
            messagebox.showerror(
                title='Sell status',
                message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
            )
            return("Failed")
        
def show_dic(dic):
    try:
        msg=""
        
        for key in dic.keys():
            if(not(type(dic[key]) is dict)):
                msg=msg+key + ": "+str(dic[key])+"\n"
                #print(type(a[key]))
            else:
                #print(dic[key])
                #pish=pish+" "
                msg=msg+key + ": "+show_dic(dic[key])#+"\n"#msg+key + ": "+"DICT"+"\n"
        return(msg)
    except Exception as e:
        print("error in show_dic()"+e.__class__.__name__+": "+str(e)) #e is a class so used str")
        
def GetToken():
    #import easygui as eg
    global myToken #to define global variable from inside of a function
    global Username
    unpw = eg.enterbox(msg="Enter Username,Password")
    tfa = eg.enterbox(msg="Enter Two Factor Authentication Code")

    if(unpw==None or tfa==None):
       #os._exit(0)
        messagebox.showerror(
            title='Get Token',
            message="to get token you should :\n1-enter username and password\n2-Enter Two Factor Authentication Code"
        )
        return(0)
    try:
        un=unpw.split(",")[0]
        pw=unpw.split(",")[1]
        tok=get_token(un,pw,tfa)
        
        myToken=tok
        Username=get_username(get_user_profile(myToken)).split("@")[0]
        print(Username," Token : ",myToken)
        showinfo(
            title='Get Token',
            message="Token : "+tok
        )
        
        return(tok)
        #print(un,"__",pw)
        
    except Exception as e:
        showerror(
            title='Get Token',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
  
def ExecuteCommand():
    showinfo(
        title='Result Message',
        message=selected_size.get()
    )

def get_lastprice2(sym_name):
    #change sym_name to uppercase beforehand to avoid error
    try:
            
        #last sym_name price
        import http.client
        #import pandas as pd
        import json
        conn = http.client.HTTPSConnection(EndPoint)
        payload = ''
        headers = {}
        tf="180" #180 minites =H3 time frame
        tto=int(get_current_unixstamp())
        tfrom=tto-1000000
        cmd="/market/udf/history?symbol=" + sym_name+"&resolution="+tf+"&from="+str(tfrom)+ "&to="+str(tto)
        conn.request("GET", cmd, payload, headers)
        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))
        #df = pd.read_json(data.decode("utf-8"))
        #print(df)
        prices=json.loads(data.decode("utf-8"))
        return(prices["c"][-1]) #close prices "c" is a list we return last price [-1]
    except:
        return(0)
    
def get_lastprice_orderbook(sym_name):
    #sym_name="BTCIRT" ,"ETCIRT",... 
    import http.client
    import json
    conn = http.client.HTTPSConnection(EndPoint)
    payload = ''
    headers = {}
    cmd="/v2/orderbook/"+sym_name
    conn.request("GET", cmd, payload, headers)
    res = conn.getresponse()
    data = res.read()
    w=data.decode("utf-8")
    #print(w)
    #string to dictionary
    dc = json.loads(w)
    #get dictioaru items (last price)
    lastp=float(dc['lastTradePrice'])
    #print("Last price:",lastp)
    return(lastp)



def append2file(filename,itemsList):
    #append elements of a list with comma delimiter to a file
    #note that
    import csv
    with open(filename, mode='a',newline='') as out_file:
        f1 = csv.writer(out_file, delimiter=',')
        f1.writerow(itemsList)
def get_dir_tree_files(mypath):
    #return list of full address of all files inside and under subdirectories in the path
    import os
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    return(listOfFiles)
def create_folder(mypath,folderName):
    import os
    try:
        # Create target Directory
        outdirName=os.path.join(mypath,folderName)
        os.mkdir(outdirName)
        print("Directory " , outdirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , outdirName ,  " already exists")
        
def readAccountsPath(filename):
    #return account pathes as a list from given file with one column format "account path"
    cnt=0
    f = open(filename, "r")
    mylist=[]

    while True:
        strlist=f.readline().split(",")
        
        if(strlist != [""]):
            accpath=strlist[0].split("\n")[0]
            mylist.append(accpath)
            cnt=cnt+1
        else:
            break       
    f.close()    
    return(mylist)
def get_current_unixstamp():
    import time
    ts = time.time()
    return(ts)

def unixstamp2date(ts):
    import datetime
    dt=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return(dt)
def unixstamp2date2(timeint):
    import datetime
    dt=datetime.datetime.fromtimestamp(timeint / 1e3).strftime('%Y-%m-%d %H:%M:%S')
    return(dt)


##get_market_trades("BTCIRT")
##get_market_trades("ETCIRT")
def get_market_stats(src1,dst1):
    import requests
    import json
    print("Market stats :", src1,"-", dst1)
    url = "https://"+EndPoint+"/market/stats"

    payload={'srcCurrency': src1,
    'dstCurrency': dst1}
    files=[

    ]
    headers = {}
    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        mkt=json.loads(response.text)
        return(mkt)
    except Exception as e:
        messagebox.showerror(
            title='Get Market Stats',
            message="Error :\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def show_market_stats():
    try:
        ww5=get_market_stats(src.get(),dst.get())
        print(ww5)   
        messagebox.showinfo(
            title='Market Stats : ' + (src.get()+"-"+dst.get()).upper(),
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Market Stats : ' + (src.get()+"-"+dst.get()).upper(),
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)

def get_market_trades(symbol):
    #return dict of given symbol market trades 
    import requests
    import json
    #to call request symbol must be in upper case contrary to buy sell requests
    url = "https://"+EndPoint+"/v2/trades/"+symbol.upper()
    print("get market trades :",symbol.upper())
    payload={}
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        tr=response.text
        trr=json.loads(tr) #string to json dict
        trades=trr["trades"] #get trades dict
        for i in trades:
            print(unixstamp2date2(i["time"]),"detail:",i)
            
        return(trr)
    except Exception as e:
        messagebox.showerror(
            title='Get Market Trades',
            message="Error :\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def show_market_trades():
    try:
        #first we have to change rls to irt in symbolname
        symbol=src.get()+dst.get()
        if(dst.get().lower()=="usdt"): 
            symbol=src.get()+"USDT"
        else: 
            symbol=src.get()+"IRT"
        ww5=get_market_trades(symbol)
        print(ww5)   
        messagebox.showinfo(
            title='Market Trades : ' + (src.get()+"-"+dst.get()).upper(),
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Market Trades : ' + (src.get()+"-"+dst.get()).upper(),
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)

def get_user_limitations():
    import requests
    import json
    global myToken
    url = url = "https://"+EndPoint+"/users/limitations"

    payload={}
    headers = {
      'Authorization': 'Token '+ myToken
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)    
        uslim=json.loads(response.text) #string to json dict
        return(uslim)
    except Exception as e:
        messagebox.showerror(
            title='Get User Limitations',
            message="Error :\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
    
def show_user_limitations():
    try:
        ww5=get_user_limitations()
        print(ww5)   
        messagebox.showinfo(
            title="User Limitations",
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='User Limitations',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def get_user_orders():
    #returns json dictionary of given order id (idu is of type string) 
    global myToken
    import requests
    import json
    url = "https://"+EndPoint+"/market/orders/list?details=2&status=all"

    payload={}
    headers = {
      'Authorization': 'Token '+myToken
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        ww5=json.loads(response.text)

        return(ww5)
    except Exception as e:
        messagebox.showerror(
            title='Get order status',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return("Failed")

def show_user_orders():
    try:
        ww5=get_user_orders()
        print(ww5)   
        messagebox.showinfo(
            title='User Orders',
            message=ww5
        )
    except Exception as e:
        messagebox.showerror(
            title='User Orders',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)

def get_user_trades():
    #returns json dictionary of given order id (idu is of type string) 
    global myToken
    import requests
    import json
    url = "https://"+EndPoint+"/market/trades/list"

    payload={}
    headers = {
      'Authorization': 'Token '+myToken
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        ww5=json.loads(response.text)

        return(ww5)
    except Exception as e:
        messagebox.showerror(
            title='User Trades',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return("Failed")

def show_user_trades():
    try:
        ww5=get_user_trades()
        print(ww5)   
        messagebox.showinfo(
            title='User Trades',
            message=ww5
        )
    except Exception as e:
        messagebox.showerror(
            title='User Trades',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)

        
def get_order_status(idu):
    
    #returns json dictionary of given order id (idu is of type string) 
    global myToken
    import requests
    import json
    url = "https://"+EndPoint+"/market/orders/status?id="+idu

    payload={}
    headers = {
      'Authorization': 'Token '+myToken
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        ww5=json.loads(response.text)
        eeid=str(ww5["order"]['status'])
        print("Check last order status : ",eeid)
        return(eeid)
    except Exception as e:
        print("Check last order status :"," Failed")
        return("Failed")
    
def get_order_detail(idu):
    
    #returns json dictionary of given order id (idu is of type string) 
    global myToken
    import requests
    import json
    url = "https://"+EndPoint+"/market/orders/status?id="+idu

    payload={}
    headers = {
      'Authorization': 'Token '+myToken
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        ww5=json.loads(response.text)
##        print(str(ww5["order"]['type']))
##        print(str(ww5["order"]['execution']))
##        print(str(ww5["order"]['tradeType']))
##        print(str(ww5["order"]['srcCurrency']))
##        print(str(ww5["order"]['dstCurrency']))
##        print("price : ",str(ww5["order"]['price']))
##        print(str(ww5["order"]['amount']))
        print("totalPrice : ",str(ww5["order"]['totalPrice']))
        print("totalOrderPrice : ",str(ww5["order"]['totalOrderPrice']))
##        print(str(ww5["order"]['matchedAmount']))
##        print(str(ww5["order"]['unmatchedAmount']))
##        print(str(ww5["order"]['isMyOrder']))
##        print(str(ww5["order"]['id']))
##        print(str(ww5["order"]['status']))
##        print(str(ww5["order"]['partial']))
##        print(str(ww5["order"]['fee']))
##        print(str(ww5["order"]['user']))
        print("averagePrice : ",str(ww5["order"]['averagePrice']))        
        print("created_at : ",str(ww5["order"]['created_at']))
##        print(str(ww5["order"]['market']))
##        eeid=str(ww5["order"]['status'])
        #print("Check last order status : ",eeid)
        return(0)
    except Exception as e:
##        messagebox.showerror(
##            title='Get order status',
##            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
##        )
        print("Check last order status :"," Failed")
        return("Failed")
    
def order_Done(res):
    global TradeAllowed
    #ww5 is dictionary of order status json data
    try:
        if(res=="Done"):
            TradeAllowed=True
            print("Order : Done\n","Trade Allowed : True")
            return(True)
        if(res=="Active"):
            TradeAllowed=False
            print("Order : Active\n","Trade Allowed : False")
            return(False)
        
    except Exception as e:
        messagebox.showerror(
            title='Order',
            message="Order Not Done\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        print("Order Not Done\n"+e.__class__.__name__+": "+str(e)) #e is a class so used str
        return(False)
    
def get_market_settings_options():
    #get status of 'status', 'features', 'coins', 'nobitex' including allcoins ,presisions ,daily monthly limitations ,...
    #get from "nobitex" sub dict all user level types daily monthly limitations and much more
    #you can get user level from get_profile function
    import requests
    import json
    url = "https://"+EndPoint+"/v2/options"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    mkt=json.loads(response.text)
    #print("\n Market :\n",mkt)
    return(mkt)

def show_market_settings_options():
    
    try:
        ww5=get_market_settings_options()
        print(ww5)   
        messagebox.showinfo(
            title='Market Options',
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Market Options',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def get_deposits():
    import requests
    import json
    url = "https://"+EndPoint+"/users/wallets/deposits/list"

    payload={}
    headers = {
        'Authorization': 'Token '+myToken
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    ww5=json.loads(response.text)
    #print("\n Market :\n",mkt)
    return(ww5)

def show_deposits():
    
    try:
        ww5=get_deposits()
        print(ww5)
        amnt=get_deposits_amounts(ww5)
        vamnt=[int(i) for i in amnt]
        total=str(sum(vamnt))
        print("\ndeposit amounts :\n",amnt, "Total :",total)

        messagebox.showinfo(
            title='Deposits'+" Total : "+total,
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Deposits',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
    
def get_deposits_amounts(ww5):
    #return list of deposit amounts 
    mylist=[]
    for dep in ww5["deposits"]:
        mylist.append(dep["amount"])
	
    return(mylist)

    
def get_withdraws():
    import requests
    import json
    url = "https://"+EndPoint+"/users/wallets/withdraws/list"

    payload={}
    headers = {
        'Authorization': 'Token '+myToken
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    ww5=json.loads(response.text)
    return(ww5)

def show_withdraws():
    
    try:
        ww5=get_withdraws()
        print(ww5)
        amnt=get_withdraws_amounts(ww5)
        vamnt=[int(i) for i in amnt]
        total=str(sum(vamnt))
        print("\nwithdraws amounts :\n",amnt, "Total :",total)
        messagebox.showinfo(
            title='Withdraws'+" Total : "+total,
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Withdraws',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
    
def get_withdraws_amounts(ww5):
    #return list of withdraw amounts 
    mylist=[]
    for dep in ww5["withdraws"]:
        mylist.append(dep["amount"])
	
    return(mylist)
    

    

def get_token(un,pw,twoFA):
    #given us and pass and 2FA returns dictionary of keys dict_keys(['status', 'key', 'expiresIn', 'device', 'we_id'])
    import requests
    import json
    url = "https://"+EndPoint+"/auth/login/"

    payload={'username': un,
    'password': pw,
    'remember': 'yes',
    'captcha': 'api',
    'useragent': 'TraderBot/your_bot'}
    files=[

    ]
    headers = {
      'X-TOTP': twoFA
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    ww4=json.loads(response.text)#string to json dict
    tkn=ww4['key']
    print("Token : ",tkn)
    return(tkn)
def burn_token():
    global myToken
    try:
        import requests
        url = "https://"+EndPoint+"/auth/logout/"
        payload={}
        headers = {
          'Authorization': 'Token '+myToken
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        messagebox.showinfo(
            title='Burn Token',
            message="Token Burned : " +myToken+"\n"+response.text
        )

    except Exception as e:
        messagebox.showerror(
            title='Burn Token',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
        
def get_user_profile(tokenKey):
    import requests
    import json
    url = "https://"+EndPoint+"/users/profile"

    payload={}
    headers = {
      'Authorization': 'Token '+tokenKey
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)
    ww5=json.loads(response.text)#string to json dict
    return(ww5)
def show_user_profile():
    global myToken
    try:
        ww5=get_user_profile(myToken)
        #Username=get_username(ww5) #set global variable "Username" from profile data
        print(ww5)   
        messagebox.showinfo(
            title='Profile Status',
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Profile Status',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def get_username(ww5):
    #global Username
    try:
        un=ww5["profile"]["username"]
        print("username :",un)
        return(un)
    except:
        print("Username could not be extracted")
        return("Guest")
    

def get_wallets_money(tokenKey):
    #to get some wallet balance use
    #wal=get_wallets_money(tokenKey)
    #wal["wallets"]["BTC"]["balance"]
    import requests
    import json
    url = "https://"+EndPoint+"/v2/wallets"

    payload={}
    headers = {
      'Authorization': 'Token '+tokenKey
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    trr=json.loads(response.text) #string to json dict
    
    #print(type(trr),trr,"\n",type(response.text),response.text)
    return(trr)

def show_wallets_money():
    global myToken
    try:
        ww5=get_wallets_money(myToken)
        print("wallets :\n",get_wallets_list(ww5))
        print(ww5)
        messagebox.showinfo(
            title='Wallet status',
            message=ww5
        )

    except Exception as e:
        messagebox.showerror(
            title='Wallet status',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def get_wallets_ids(ww5):
    #return list of wallets ids as a list: [123454,623454,...] for later use
    mylist=[]
    for w in ww5["wallets"]:
        mylist.append(ww5["wallets"][w]["id"])
	
    return(mylist)

def get_wallets_list(ww5):
    #return list of wallets names : ["BTC","ETH",...]
    mylist=[]
    for w in ww5["wallets"]:
        mylist.append(w)
	
    return(mylist)	

def get_wallet_transactions(id):
    #return transactions of a wallet given wallet id
    global myToken
    import requests
    import json
    try:
        import requests
        url = "https://"+EndPoint+"/users/wallets/transactions/list?wallet=" + str(id)
        payload={}
        headers = {
          'Authorization': 'Token '+myToken
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        ww5=json.loads(response.text)
        #print(ww5)
        return(ww5)
    except Exception as e:
        messagebox.showerror(
            title='Wallet Transaction id:'+str(id),
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)

def get_wallets_transactions():
    #return transactions of all wallets !!!! dosnt merge dics !!!! just print
    global myToken
    import requests
    import json
    try:
        ww_all={}#empty dic
        ww5=get_wallets_money(myToken)#get wallets dictionary
        ids=get_wallets_ids(ww5)
        ww_all=[]
        for i in ids:
            ww6=get_wallet_transactions(i)
            ww_all.append(ww6)
            
        messagebox.showinfo(
            title='Wallets Transactions',
            message=ww_all
        )
    
        return(ww_all)    
    except Exception as e:
        messagebox.showerror(
            title='Wallets Transactions',
            message="Something is wrong\n"+e.__class__.__name__+": "+str(e) #e is a class so used str
        )
        return(0)
def request_withdraw():
    print("Request  Withdraw ... To be developed")
    
def Buy_Market(srcCurrency,dstCurrency,amount,price,stopPrice,Token,EndPoint):
#all arguments must be string
    import requests
    import json
    url = "https://"+EndPoint+"/market/orders/add"

    payload={'type': 'buy',
    'execution': 'market',
    'srcCurrency': srcCurrency,#"bnb"
    'dstCurrency': dstCurrency,#'rls',
    'amount': amount,#'0.01',
    'price': price,
    'stopPrice': stopPrice}
    files=[

    ]
    headers = {
      'Authorization': 'Token '+Token
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    ww5=json.loads(response.text)#string to json dict
    print("buy response :",ww5)
    return(ww5)

def Sell_Market(srcCurrency,dstCurrency,amount,price,stopPrice,Token,EndPoint):
#all arguments must be string
    import requests
    import json
    url = "https://"+EndPoint+"/market/orders/add"

    payload={'type': 'sell',
    'execution': 'market',
    'srcCurrency': srcCurrency,#"bnb"
    'dstCurrency': dstCurrency,#'rls',
    'amount': amount,#'0.01',
    'price': price,
    'stopPrice': stopPrice}
    files=[

    ]
    headers = {
      'Authorization': 'Token '+Token
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    ww5=json.loads(response.text)#string to json dict
    print("sell response :",ww5)
    return(ww5)

    
def Start_trade():
    global TradeAllowed
    TradeAllowed=True
    print("Trade Started")
    button17.configure(bg="grey56", fg= "white")
##############################################################################################
def read_GD_file(url): #read shared for everyone google drive file
    try:
        import requests
        file_id = url.split('/')[-2]
        dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
        ww = requests.get(dwn_url).text
        gg=ww.split(sep=",")#split comma seperated string into a list
        stamp0=int(gg[0])
        stamp1=int(gg[1])
        return(stamp0,stamp1) #tuple of two values
    except:
        return(0,0) #tuple of two values
    
def get_tm_ntp():
    import ntplib
    import datetime, time
    try:

        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        Internet_date_and_time = datetime.datetime.fromtimestamp(response.tx_time)
        stamp=datetime.datetime.fromisoformat(Internet_date_and_time.strftime('%Y-%m-%d %H:%M:%S')).timestamp()
        #print("stamp=",stamp)
        return(stamp)
    except:
        stamp=10
        #print("stamp=",stamp)
        return(stamp)
    
def check_tm_ntp(Deadline): #deadline in seconds
    try:
        if(get_tm_ntp()>Deadline):
            #print("get_tm_ntp=",get_tm_ntp())
            return(False)
        else:
            #print("get_tm_ntp=","_______")
            return(True)    
    except:
        print("get_tm_ntp=","__excep__")
        return(False)
#usage :
    
##    ##read two integer from a file shared in my google drive  for everyone
##    ##they are deadlines in seconds from 1 jan 1970 ,then read true current time from ntp server
##    ##if current time is less than dead line user is authorized (check_tm_ntp returns True)
##    url='https://drive.google.com/file/d/1LAriMd4_ekSkXMYqQLm6P6alrgVlfPw0/view?usp=sharing'
##    qa=read_GD_file(url)
##    ##print(qa[0])
##    ##print(qa[1])
##    deadline1=qa[0]
##    deadline2=qa[1]
##    Authorized1=check_tm_ntp(deadline1)
##    Authorized2=check_tm_ntp(deadline2)
##    print("auth1:",Authorized1)
##    print("auth2:",Authorized2)
##############################################################################################
def Authorized_user():
    try:
        
        url='https://drive.google.com/file/d/1sX-Nq2sWHSfYT4rt9qNpMm2s-pacqfDD/view?usp=share_link'
        qa=read_GD_file(url)
        deadline1=qa[0]
        deadline2=qa[1]
        #print("read :",deadline1,deadline1)
        Authorized1=check_tm_ntp(deadline1)
        #Authorized2=check_tm_ntp(deadline2)
        print("Nobitex Connection1:",Authorized1)
        #print("auth2:",Authorized2)
        return(Authorized1)
    
    except:
        return(False)



##################################################################################################
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox 
import os
import time
import easygui as eg
global myToken
global layer
global TradeAllowed
global Username
global Lastid
global order_price
Lastid="None"
order_price=""
TradeAllowed=False
myToken = eg.enterbox(msg="Enter Token")
if(myToken==None):
    os._exit(0)
#set Username for window title    

if(len(myToken) !=0):
   print("Token : ",myToken)
   Username=get_username(get_user_profile(myToken)).split("@")[0]
else:
   Username="Guest"
   
if(not Authorized_user()):
    os._exit(0)
    
window = tk.Tk()

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
w = 750 # width for the Tk root
h = 250  # height for the Tk root
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))   

canvas = tk.Canvas(window,bg="white",width=700, height=585, highlightthickness=0)
canvas.pack()


R3 = tk.Label(canvas, text="R3", font="Calibri 12", bg="white")
canvas.create_window(15,10, window=R3, anchor=tk.NW)

VR3 = tk.DoubleVar()
entry_VR3 = ttk.Entry(canvas, textvariable=VR3)
entry_VR3.config({"background": "gainsboro"})
canvas.create_window(200,20, window=entry_VR3)


R2 = tk.Label(canvas, text="R2", font="Calibri 12", bg="white")
canvas.create_window(15,30, window=R2, anchor=tk.NW)

VR2 = tk.DoubleVar()
entry_VR2 = ttk.Entry(canvas, textvariable=VR2)
entry_VR2.config({"background": "gainsboro"})
canvas.create_window(200,40, window=entry_VR2)


R1 = tk.Label(canvas, text="R1", font="Calibri 12", bg="white")
canvas.create_window(15,50, window=R1, anchor=tk.NW)

VR1 = tk.DoubleVar()
entry_VR1 = ttk.Entry(canvas, textvariable=VR1)
entry_VR1.config({"background": "gainsboro"})
canvas.create_window(200,60, window=entry_VR1)

S1 = tk.Label(canvas, text="S1", font="Calibri 12", bg="white")
canvas.create_window(15,70, window=S1, anchor=tk.NW)

VS1 = tk.DoubleVar()
entry_VS1 = ttk.Entry(canvas, textvariable=VS1)
entry_VS1.config({"background": "gainsboro"})
canvas.create_window(200,80, window=entry_VS1)

S2 = tk.Label(canvas, text="S2", font="Calibri 12", bg="white")
canvas.create_window(15,90, window=S2, anchor=tk.NW)

VS2 = tk.DoubleVar()
entry_VS2 = ttk.Entry(canvas, textvariable=VS2)
entry_VS2.config({"background": "gainsboro"})
canvas.create_window(200,100, window=entry_VS2)

S3 = tk.Label(canvas, text="S3", font="Calibri 12", bg="white")
canvas.create_window(15,110, window=S3, anchor=tk.NW)

VS3 = tk.DoubleVar()
entry_VS3 = ttk.Entry(canvas, textvariable=VS3)
entry_VS3.config({"background": "gainsboro"})
canvas.create_window(200,120, window=entry_VS3)

###############
srcw = tk.Label(canvas, text="Source", font="Calibri 12", bg="white")
canvas.create_window(15,130, window=srcw, anchor=tk.NW)

src = tk.StringVar()
entry_src = ttk.Entry(canvas, textvariable=src)
entry_src.config({"background": "gainsboro"})
canvas.create_window(200,140, window=entry_src)

dstw = tk.Label(canvas, text="Destination", font="Calibri 12", bg="white")
canvas.create_window(15,150, window=dstw, anchor=tk.NW)

dst = tk.StringVar()
entry_dst = ttk.Entry(canvas, textvariable=dst)
entry_dst.config({"background": "gainsboro"})
canvas.create_window(200,160, window=entry_dst)
###############
amount = tk.Label(canvas, text="amount", font="Calibri 12", bg="white")
canvas.create_window(135,170, window=amount, anchor=tk.NW)

Vamount = tk.DoubleVar()
entry_Vamount = ttk.Entry(canvas, textvariable=Vamount)
entry_Vamount.config({"background": "gainsboro"})
canvas.create_window(200,200, window=entry_Vamount)

###################


selected_order = tk.StringVar()
orders =    (
                ('Open Buy', '220'),
                ('Open Sell', '221')
             )
# radio buttons


# buttons
#set initial values
VR3.set(0)#get_lastprice2("ETCIRT"))
VR2.set(0)
VR1.set(0)
VS1.set(0)
VS2.set(0)
VS3.set(0)
src.set("etc")
dst.set("rls")
layer="None"
################################
##button1 = tk.Button(text='Buy', command=RunBuy, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
##canvas.create_window(60, 200, window=button1)
##button3 = tk.Button(text='Sell', command=RunSell, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
##canvas.create_window(60, 230, window=button3)

button2 = tk.Button(text='Get Token        ', command=GetToken, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 20, window=button2)

button4 = tk.Button(text='User Wallets     ', command=show_wallets_money, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 50, window=button4)

button5 = tk.Button(text='User Profile     ', command=show_user_profile, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 80, window=button5)

button6 = tk.Button(text='Market Trades    ', command=show_market_trades, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 110, window=button6)

button7 = tk.Button(text='Market Options   ', command=show_market_settings_options, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 140, window=button7)

button8 = tk.Button(text='User Limitations ', command=show_user_limitations, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 170, window=button8)

button16 = tk.Button(text='Market Stats    ', command=show_market_stats, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(500, 200, window=button16)

button9 = tk.Button(text='Burn Token       ', command=burn_token, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 20, window=button9)

button10 = tk.Button(text='Deposits         ', command=show_deposits, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 50, window=button10)

button11 = tk.Button(text='Orders           ', command=show_user_orders, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 80, window=button11)

button12 = tk.Button(text='Trades           ', command=show_user_trades, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 110, window=button12)

button13 = tk.Button(text='Request Withdraw ', command=request_withdraw, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 140, window=button13)

button14 = tk.Button(text='Withdraws        ', command=show_withdraws, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 170, window=button14)

button15 = tk.Button(text='Transactions     ', command=get_wallets_transactions, bg='brown', fg='white', font=('helvetica', 7, 'bold'))
canvas.create_window(630, 200, window=button15)

button17 = tk.Button(text='Start     ', command=Start_trade, bg='brown', fg='white', font=('helvetica', 7, 'bold'),activebackground="blue")
canvas.create_window(300, 230, window=button17)


################################
clock = tk.Label(window, font=("none", 10, "bold"), bg="grey78", fg="black", bd=1, relief="ridge")
canvas.create_window(135, 230, window=clock)
tick()
window.mainloop()
