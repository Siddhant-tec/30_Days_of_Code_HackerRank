import numpy as np
dog_breed_dict = {'Labrador Retriever': 5, 'German Shepherd': 12, 'Beagle': 10}
check = ['German Shepherd','Beagle']
for name in dog_breed_dict.keys():
    if name in check:
        print(name)
        print(dog_breed_dict[name])
