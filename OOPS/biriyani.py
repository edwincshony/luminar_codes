class Biriyani:

    # title: str
    # category: str
    # price: int

    def set_biriyani(self,title,category,price):

        self.title = title
        self.category = category
        self.price = price

    def display(self):

        print(self.title,self.category,self.price)

malabar_biriyani_instance = Biriyani()
hyderabadi_biriyani_instance = Biriyani()

malabar_biriyani_instance.set_biriyani("malabari biriyani","dum",180)
hyderabadi_biriyani_instance.set_biriyani("hyderabad biriyani","chicken",300)

malabar_biriyani_instance.display()
hyderabadi_biriyani_instance.display()