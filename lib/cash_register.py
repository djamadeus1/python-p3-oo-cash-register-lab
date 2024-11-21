#!/usr/bin/env python3

      # Creating a virtual Cassh register
class CashRegister:         
    def __init__(self, discount=0):   # Uing Dunder method int to set attributes to our Cash register class
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, name, price, quantity=1):
            self.total += price * quantity 
            self.last_transaction = price * quantity
            self.items.extend([name] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
              print("There is no discount to apply.")

        # if not isinstance(self.discount, (int,float)):
        #      raise TypeError("Must be a number")
       
    def void_last_transaction(self):
           self.total -= self.last_transaction

          


           
                   

    