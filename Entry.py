import pyautogui as pg
import time as t
import pyperclip as pycl
import requests
import json
from pynput.keyboard import Key,Controller

from DataExtractor import DataExtractor

keyboard = Controller()

def select():

    pg.doubleClick()
    t.sleep(0.5)
    

def run():

    de = DataExtractor()
    de.extractData()
    purchaseOrders = de.getData()

    start()

    for i in range(len(purchaseOrders)):

        po = purchaseOrders[i]
        if(i != 0):
            pg.moveTo(25,230)
            t.sleep(1)
            select()

        t.sleep(3)
        orgData(po)

        supplier(po)

        text(po)
    
        deliveryInvoice(po)

        t.sleep(1)
        pg.moveTo(35, 230)
        select()

        for i in range(len(po["items"])):
             
            enterItems(po["items"][i], i)
            t.sleep(2)
            brazil(po)
            
            accountAssignment(po)

        end([po["ID"], getSAPNumber(),po["RequesterId"]])




def enterItems(item, itemNum):

    t.sleep(1)
    pg.moveTo(180,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(item["A"])

    t.sleep(3)

    pg.moveTo(520,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(item["shortText"])

    t.sleep(3)

    pg.moveTo(700,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(item["poQuantity"])

    t.sleep(3)

    pg.moveTo(810,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(item["unit"])

    t.sleep(3)

    pg.moveTo(930,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(item["deliveryDate"])

    t.sleep(3)

    pg.moveTo(1050,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(str(item["netPrice"]))

    t.sleep(3)

    pg.moveTo(1350,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type("1099")

    t.sleep(3)

    pg.moveTo(1500,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type("6071")

    
    t.sleep(3)
    
    pg.moveTo(220,830)
    pg.click(clicks=3, interval=0.5)

    t.sleep(3)

    pg.moveTo(1460,300 + (35 * itemNum))
    t.sleep(0.2)
    pg.click()
    t.sleep(1)
    keyboard.type(item["ReqmtNo"])

    t.sleep(2)
    pg.moveTo(240,830)
    pg.click()


def start():
    

    pg.click()
    print(pg.position())
    pg.click(180,130)
    print(pg.position())
    t.sleep(2)
    keyboard.type("redacted")
    t.sleep(0.1)

    pg.hotkey("enter")
    
    t.sleep(5)


def supplier(purchaseOrder):

    t.sleep(1)
    keyboard.type(purchaseOrder["SupplierNum"])
    t.sleep(0.3)
    pg.hotkey("enter")


def orgData(purchaseOrder):

    t.sleep(2)

    pg.moveTo(1080,230)
    select()

    t.sleep(2)

    pg.moveTo(260,300)
    select()
    t.sleep(2)
    keyboard.type(purchaseOrder["Purch. Org."])
    
    t.sleep(2)

    pg.hotkey("enter")

    t.sleep(2)

    pg.moveTo(255,330)
    t.sleep(2)
    select()
    t.sleep(2)
    keyboard.type(purchaseOrder["Purch. Group"])
    t.sleep(2)
    pg.hotkey("enter")

    t.sleep(2)


def deliveryInvoice(purchaseOrder):

    t.sleep(2)

    pg.moveTo(150,240)
    select()

    pg.moveTo(280,300)
    select()
    t.sleep(1)
    keyboard.type(purchaseOrder["PaymentTerms"])

    t.sleep(1)

    pg.hotkey("enter")

    t.sleep(1)

    pg.moveTo(285,430)
    select()
    t.sleep(1)
    keyboard.type(purchaseOrder["incoterms"][1])

    t.sleep(1)
    
    pg.moveTo(600, 430)
    select()
    t.sleep(0.5)
    pg.moveTo(303, 430)
    pg.mouseDown()
    t.sleep(0.5)
    pg.moveTo(600, 430)
    t.sleep(1)
    keyboard.type(purchaseOrder["incoterms"][0])


def brazil(purchaseOrder):
    pg.hotkey("enter")
    t.sleep(1)

    pg.moveTo(1020,640)
    t.sleep(0.5)
    pg.click()
    t.sleep(1)

    pg.moveTo(240,700)
    pg.click()
    t.sleep(1)
    keyboard.type(purchaseOrder["materialUsage"])
    t.sleep(0.5)
    pg.hotkey("enter")
    t.sleep(1)

    pg.moveTo(680,700)
    pg.click()
    t.sleep(1)
    keyboard.type(purchaseOrder["MatCat"])
    t.sleep(0.5)
    pg.hotkey("enter")
    t.sleep(1)

    pg.moveTo(240,735)
    pg.click()
    t.sleep(1)
    keyboard.type(purchaseOrder["matOrigin"])
    t.sleep(1)

    pg.moveTo(280,770)
    t.sleep(0.5)
    pg.doubleClick()
    t.sleep(1)
    pg.moveTo(370,770)
    pg.mouseDown()
    t.sleep(0.5)
    pg.moveTo(240,770)
    pg.mouseUp()
    t.sleep(1)
    keyboard.type(purchaseOrder["NCMCode"])
    t.sleep(0.5)
    pg.hotkey("enter")

    t.sleep(3)


def accountAssignment(purchaseOrder):

    t.sleep(3)

    pg.moveTo(300,670)
    select()
    keyboard.type(purchaseOrder["GLAccount"])
    t.sleep(0.5)
    pg.hotkey("enter")
    t.sleep(1)
    
    pg.moveTo(300,730)
    t.sleep(0.5)
    pg.click()
    t.sleep(1)
    keyboard.type(purchaseOrder["Order"])
    pg.hotkey("enter")
    t.sleep(1)

    pg.moveTo(30,500)
    select()


def text(purchaseOrder):

    t.sleep(2)
    pg.moveTo(390,235)
    select()
    t.sleep(2)
    pg.moveTo(700,340)
    t.sleep(0.5)
    pg.click()
    t.sleep(0.5)
    keyboard.type(purchaseOrder["LongText"])



def getSAPNumber():
    t.sleep(3)
    pg.moveTo(300,130)
    t.sleep(0.5)
    pg.click()


    t.sleep(3)
    pg.moveTo(385,990)
    t.sleep(0.5)
    pg.click()
    t.sleep(0.5)
    pg.mouseDown()
    t.sleep(0.5)
    pg.moveTo(485,990)
    pg.mouseUp()
    t.sleep(0.5)
    pycl.copy("")
    t.sleep(0.1)
    pg.hotkey("ctrl", "c")
    t.sleep(0.1)
    sapNum = pycl.paste()
    
    return sapNum


def end(donePO):

    url = f"redacted"
    
    response = requests.put(url, json={"pr_id": donePO[0] ,"purchase_request_pon": donePO[1],
                                        "requester_id" : donePO[2], "status": 5})


