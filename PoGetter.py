import requests


class POGetter():


    def __init__(self):
        self.rawData = requests.get("redacted").json()
        self.purchaseOrders = []
        self.validStatus = 5


    def requestOpenPOs(self):

        for po in self.rawData:

            if po["status"] == self.validStatus:
                self.purchaseOrders.append(po)
        

    def getPOs(self):
        return self.purchaseOrders.copy()

