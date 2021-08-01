class Dog:
    dog_breed_dict = {'Labrador Retriever': 5, 'German Shepherd': 12, 'Beagle': 10}

    def __init__(self, breed_list):
        self.breed_list = breed_list
        self.dog_id_list = ['lo']
        self.price = 0
        self.access_required = bool

    def validate_breed(self):
        if set(self.breed_list).issubset(self.dog_breed_dict.keys()):
            return True
        else:
            return False

    def validate_quantity(self):
        for name in self.dog_breed_dict.keys():
            if name in self.breed_list:
                return True
            else:
                return False

    def get_dog_price(self):
        for breed in self.breed_list:
            if breed == 'Labrador Retriever':
                self.price = 80
            if breed == 'German Shepherd':
                self.price = 1230
            if breed == "Beagle":
                self.price = 650

    def calculate_total_price(self):
        if self.validate_quantity() and self.validate_breed() == True:
            self.get_dog_price()


dog_breeds = ['German Shepherd', 'Labrador Retriever', 'Beagle']
dog = Dog(dog_breeds)
dog.validate_quantity()
dog.validate_breed()
print(dog.validate_breed())
dog.get_dog_price()

