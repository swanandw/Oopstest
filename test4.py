class Person :


    def age(self,current_age,year_of_birth):
        return  current_age-year_of_birth

    def email_id_input(self,emailid):
        print("take and mail id form a person and print it", emailid)

    def ask_name(self):
        name = input("tell me name")
        return name

    def ask_dob(self):
        dob = input("tell me dob")
        return dob


sudh= Person()
anuj = Person()
gargi= Person()
hitesh = Person()

sudh.email_id_input("sudhanshu@ineuron.ai")

print(sudh.ask_name())