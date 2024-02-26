class University:
    def Register(self,sid,sname,sphone,saddress):
        self.s_id=sid
        self.s_name=sname
        self.s_phone=sphone
        self.s_address=saddress

    def Display(self):
        print(self.s_id)
        print(self.s_name)
        print(self.s_phone)
        print(self.s_address)

# un=University()
# un.Register('001','dal','98547','ktm')
# un.Display()
