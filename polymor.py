class Poly:
    def __init__(self,name):
        self.uname=name
    def Reg(self,uid):
        self.u_id=uid

    def Reg(self,uid,uname,uphone):
        self.u_id=uid
        self.u_name=uname
        self.u_phone=uphone

    def Reg(self,uid,uname,uphone,uaddress):
        self.u_id=uid
        self.u_name=uname
        self.u_phone=uphone
        self.u_address=uaddress


    def Show(self):
        print(self.u_id)
    def Show(self):
        print(self.u_id)
        print(self.u_name)
        print(self.u_phone)
    def Show(self):
        print(self.u_id)
        print(self.u_name)
        print(self.u_phone)
        print(self.u_address)
