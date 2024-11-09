'''
from abc import ABC,abstractmethod
class Customer:
    def __init__(self,customer_id,customer_name,customer_mail):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.customer_mail=customer_mail
        
class Product:
    def __init__(self,product_id,product_name,product_price):
        self.product_id=product_id
        self.product_name=product_name
        self.product_price=product_price
class Order:
    def __init__(self,order_id,customer,product):
        self.order_id=order_id
        self.customer=customer
        self.product=product
        self.__payment_status="pending"
    def get_payment_status(self):
        return self.__payment_status
    def set_payment_status(self,payment_status):
        self.__payment_status=payment_status
class payment_type(ABC):
    @abstractmethod
    def payment(self):
        pass
class Credit_card(payment_type):
    def payment(self):
        print("Payment is done using credit card")
class Debit_card(payment_type):
    def payment(self):
        print("Payment is done using debit card")
class physical_product(Product):
    def __init__(self,product_id,product_name,product_price,product_weight):
        super().__init__(product_id,product_name,product_price)
        self.product_weight=product_weight
class digital_product(Product):
    def __init__(self,product_id,product_name,product_price,product_size):
        super().__init__(product_id,product_name,product_price)
        self.product_size=product_size
c1=Customer(1,"Gayathri","gayathri@gmail.com")
p1=Product(101,"Laptop",1000)
o1=Order(1,c1,p1)
o1.set_payment_status("paid")
print(o1.get_payment_status())
c1=Credit_card()
c1.payment()
d1=Debit_card()
d1.payment()
'''
'''
from abc import ABC,abstractmethod
class Book:
    def __init__(self,title,author,id):
        self.title=title
        self.author=author
        self.id=id
        self.is_available=True
class Book_type(ABC):
    @abstractmethod
    def book_type(self):
        pass
class Fiction(Book,Book_type):
    def __init__(self,title,author,id):
        super().__init__(title,author,id)
    def book_type(self):
        print("Book is of Fiction type")
    def get_details(self):
        return f"{self.title} by {self.author} (Physical Copy)"
class Non_fiction(Book,Book_type):
    def __init__(self,title,author,id):
        super().__init__(title,author,id)
    def book_type(self):
        print("Book is of Non-fiction type")
    def get_details(self):
        return f"{self.title} by {self.author} (E-Book, 5MB)"
def print_book_details(book):
    print(book.get_details())
class Member:
    def __init__(self,member_id,member_name):
        self.member_id=member_id
        self.member_name=member_name
class Loan:
    def __init__(self,book,member):
        self.book=book
        self.member=member
        self.__loan_date=None
        self.__return_date=None
    def set_loan_date(self,loan_date):
        self.__loan_date=loan_date
        self.book.is_available=False
    def set_return_date(self,return_date):
        self.__return_date=return_date
        self.book.is_available=True
    def get_loan_date(self):
        return self.__loan_date
    def get_return_date(self):
        return self.__return_date
    



b1=Book("The Alchemist","Paulo Coelho",1)
b2=Book("To Kill a Mockingbird","Harper Lee",2)
m1=Member(1,"Gayathri")
l1=Loan(b1,m1)
l2=Loan(b2,m1)
print(l1.book.author)
print(l1.member.member_name)
l1.set_loan_date("2024-01-01")
print(l1.get_loan_date())
l2.set_loan_date("2024-01-02")
print(l2.get_loan_date())
l1.set_return_date("2024-01-02")
print(l1.get_return_date())
print(l1.book.is_available)
print(l2.book.is_available)
t1=Fiction("The Alchemist","Paulo Coelho",1)
t2=Non_fiction("To Kill a Mockingbird","Harper Lee",2)
t1.book_type()
t2.book_type()
print_book_details(t1)  
print_book_details(t2)          
 '''
"""Crop Management: Need to track the type of crops grown, their growth stages, and the amount of water, fertilizer, and pesticide used.
Irrigation Management: Monitor water usage and control irrigation systems based on weather and soil conditions.
Machinery Maintenance: Keep track of different types of farm machinery (e.g., tractors, plows) and their maintenance schedules.
Worker Management: Assign tasks to workers based on their skills and monitor their work progress.
Reporting and Alerts: Generate reports on crop yield, water usage, and equipment status, and receive alerts for required actions like irrigation or equipment maintenance."""
from abc import ABC,abstractmethod
class crop:
    def __init__(self,crop_name,crop_stage):
        self.crop_name=crop_name
        self.crop_stage=crop_stage
        self.__water_needed=0
    def set_water_needed(self,water_needed):
        if water_needed>0:
            self.__water_needed=water_needed
    def get_water_needed(self):
        return self.__water_needed
        
class worker:
    def __init__(self,worker_name,skill):
        self.worker_name=worker_name
        self.skill=skill
class machinary():
    def __init__(self,type,last_serviced):
        self.type=type
        self.last_serviced=last_serviced
class FarmEquipment(ABC):
    @abstractmethod
    def perform_task(self):
        pass
class Tractor(machinary,FarmEquipment):
    def __init__(self,type,last_serviced):
        super().__init__(type,last_serviced)
    def perform_task(self):
        print("Tractor is performing task")
class Harvester(machinary,FarmEquipment):
    def __init__(self,type,last_serviced):
        super().__init__(type,last_serviced)
    def perform_task(self):
        print("Harvester is performing task")


crop1=crop("Tomato","Seedling")
worker1=worker("Gayathri","Gardening")
machinary1=machinary("Tractor","2024-01-01")
print(crop1.crop_name)
print(worker1.worker_name)
print(machinary1.type)  
crop1.set_water_needed(10)
print(crop1.get_water_needed())
t1=Tractor("Tractor","2024-01-01")  
h1=Harvester("Harvester","2024-01-01")
t1.perform_task()
h1.perform_task()

