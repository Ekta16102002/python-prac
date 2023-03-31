#Derived HDFCBank class from Bank class with two methods and two object
#parent class
class bank():
def  init (self, Accountholdername):
    self.Accountholdername=Accountholdername
class HDFCbank(bank):
def  init (self, Accountnumber,Accountholdername):
      self.Accountnumber=Accountnumber
    bank. init (self, Accountholdername)
def print info(self):
    print(self.Accountnumber)
    print(self.Accountholdername)
s1=HDFCbank('Ekta singh',"7021142799")
s1.print info()

#33_ITB_EKTA SINGH