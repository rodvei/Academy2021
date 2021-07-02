class Person(object):
    default_domain = 'online.com'
    
    def __init__(self, first, last, birth_year, domain=None):
        self.first = first
        self.last = last
        self.birth_year = birth_year
        self.domain = domain
        if domain is None:
            self.email = f'{first}.{last}@{self.default_domain}'
        else:
            self.email = f'{first}.{last}@{domain}'
    def full_name(self):
        """
        Gets the full name of the person
        """
        first = self.first.capitalize()
        last = self.last.capitalize()
        output = f'{first} {last}'
        return(output)
    
    def age(self):
        """
        Calculates the age of the person
        """
        age = 2021-self.birth_year
        return(age)
    
    def legal(self):
        """
        Check if the person is over 18 and prints if the person ar allowed to 
        drink
        """
        if self.age() > 18:
            print(f'{self.full_name()} can drink')
        else:
            print(f'{self.full_name()} can not drink!')
    
    def __len__(self):
        """
        gets the full name length
        """
        return(len(self.full_name()))
    
    def __repr__(self):
        """
        returns a string of how to create itself
        """
        class_name = self.__class__.__name__
        return(f'{class_name}("{self.first}", "{self.last}", {self.birth_year}, {self.domain})')

me = Person('kristoffer', 'rodvei', 1989)
me.email
me.full_name()
me.age()
me.legal()
len(me)
print(me)
# Person("kristoffer", "rodvei", 1989, None)

