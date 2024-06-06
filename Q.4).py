class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number


class IndividualCustomer(Person):
    def __init__(self, cust_id, name, email, phone_number, credit_class, discounts, plan_assigned):
        super().__init__(name, email, phone_number)
        self.cust_id = cust_id
        self.credit_class = credit_class
        self.discounts = discounts
        self.plan_assigned = plan_assigned


class CompanyCustomer(Person):
    def __init__(self, cust_id, name, email, phone_number, relationship_manager, credit_line, extensions, numbers):
        super().__init__(name, email, phone_number)
        self.cust_id = cust_id
        self.relationship_manager = relationship_manager
        self.credit_line = credit_line
        self.extensions = extensions
        self.numbers = numbers


class Vendor:
    def __init__(self, vendor_id, name, email, phone_number, products_supplied):
        self.vendor_id = vendor_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.products_supplied = products_supplied
	
