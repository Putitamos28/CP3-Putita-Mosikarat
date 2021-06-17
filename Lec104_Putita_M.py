class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to ",self.name, self.lastname,"'s cart", )

customer1 = Customer()
customer1.name = "Putita"
customer1.lastname = "Mosikarat"
customer1.age = 21
customer1.addCart()

customer2 = Customer()
customer2.name = "Dhi"
customer2.lastname = "Geramethakul"
customer2.age = 21
customer2.addCart()

customer3 = Customer()
customer3.name = "Gochakon"
customer3.lastname = "Saengjun"
customer3.age = 21
customer3.addCart()