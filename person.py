class Address:
    'This class represents an address'
    def __init__(self, number, street, city, postcode):
        self.number = number
        self.street = street
        self.city = city
        self.postcode = postcode
    def address(self):
        return self.number + ' ' + self.street + ' ' + self.city + ' ' + self.postcode


class Person:
    'This class represents a person'
    def __init__(self, first_name, surname, dob, address):
        self.first_name = first_name
        self.surname = surname
        self.dob = dob
        self.address = address
    def full_name(self):
        return self.first_name +' '+ self.surname


class Detective(Person):
    def __init__(self, first_name, surname, dob, address, assistant):
        Person.__init__(self, first_name, surname, dob, address)
        self.assistant = assistant
