class Person :


    def __init__(self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def age(self,current_year):
        return current_year - self.year_of_birth


anuj_var = Person("anuj","bhandari","anuj@gmail.com","1994")
sudh = Person("sudhanshu","kumar","sudhanshu@gmail.com","1994")
gargi = Person("sudhanshu","kumar","sudhanshu@gmail.com","1994")


print(sudh.age(2022))

print(sudh.name+sudh.surname)
print(anuj_var.name)
print(sudh.surname)
print(gargi.emailid)
print(anuj_var.year_of_birth)

print(type(sudh))
