class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]  # Allowed pet types
    all = []  # Class variable to store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.owner = owner  # Optional owner
        if owner:
            owner.add_pet(self)
        Pet.all.append(self)  # Add instance to the class variable all


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # List to hold pets of this owner

    def pets(self):
        return self._pets  # Return the owner's pets

    def add_pet(self, pet):
        if isinstance(pet, Pet):  # Check if pet is an instance of Pet
            pet.owner = self  # Assign this owner to the pet
            self._pets.append(pet)
        else:
            raise Exception("Only instances of Pet can be added.")

    def get_sorted_pets(self):
        # Return pets sorted by name
        return sorted(self._pets, key=lambda pet: pet.name)
