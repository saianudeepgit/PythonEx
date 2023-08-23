class CompanyClass:
    companyname="ABC"
    companyRegistration="PVT LTD"
    companyAddress="XYZ"
    companySize=100
    companyLocation="ABCDEFGH"
def DisplayCompanyDetails(self):
    print("the company details are:","\n"+self.companyName+"\n"+self.companyRegistration+"\n"+
          self.companyAddress+"\n"+self.companySize+"\n"+self.companyLocation+"\n")
def UpdateCompanyAddress(self):
    self.companyAddress=input("enter company adress:")
    print("the company address is:")