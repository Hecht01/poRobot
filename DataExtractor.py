import PoGetter as POG
import Utils

class DataExtractor():


    def __init__(self):
        
        self.rawPOs = []

        self.Data = []

        self.retrievePOs()


    def retrievePOs(self):

        pog = POG.POGetter()
        pog.requestOpenPOs()
        self.rawPOs = pog.getPOs()



    def extractData(self):

        for po in self.rawPOs:
            POinfo = {}
            POinfo["ID"] = po["pr_id"]
            POinfo["SupplierNum"] = po["supplier_vendor_number"]
            POinfo["PaymentTerms"] = po["payment_condition"]
            POinfo["RequesterId"] = po["requester_id"]
            POinfo["incoterms"] = [po["shipper"], po["shipping_type"]]
            POinfo["Purch. Org."] = "6071"
            POinfo["Purch. Group"] = "103"
            POinfo["Company Code"] = "6071"
            POinfo["matGroup"] = "1099" 
            POinfo["plant"] = "6071"
            POinfo["MatCat"] = "0"
            POinfo["materialUsage"] = "2"
            POinfo["matOrigin"] = "0"
            POinfo["NCMCode"] = "DIVERSOS"
            POinfo["GLAccount"] = "600010"
            POinfo["Order"] = "200000"
            POinfo["LongText"] = po["observations"]            
            POinfo["items"] = []
            for item in po["items"]:
                dict = {}
                dict["A"] = "F"
                dict["shortText"] = item["description"]
                dict["poQuantity"] = item["quantity"]
                dict["unit"] = item["measurement_unit"]
                dict["netPrice"] = str(round(item["subtotal"],2)).replace(".", ",")
                dict["deliveryDate"] = Utils.formatDate(item["estimated_receive_date"])
                costCenterCode = po["cost_center"].split(" - ")[1]
                NN = ""
                if(po["refunded_by_client_option"]== "with_po"):
                    NN = ";NN"

                dict["ReqmtNo"] = po["expense_control"] + ";" + costCenterCode + NN
                POinfo["items"].append(dict)
            
            self.Data.append(POinfo)    


    def getData(self):
        return self.Data
    
