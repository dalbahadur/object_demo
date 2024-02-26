from polymor import Poly as pl

class Calling:
    def Polycall(self):
        uid=input("Enter university id")
        uname=input("Enter university name")
        uphone=input("Enter university phone")
        uaddress=input("Enter university address")
        ply = pl('t.u')
        ply.Reg(uid,uname,uphone,uaddress)
        ply.Show()

newcall=Calling()
newcall.Polycall()
