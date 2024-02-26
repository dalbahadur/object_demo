from universitymodule import University as uno

sid=input("Enter sid")
sname=input("Enter name")
sphone=input("Enter phone")
saddress=input("Enter address")

un = uno()
un.Register(sid,sname,sphone,saddress)
un.Display()






