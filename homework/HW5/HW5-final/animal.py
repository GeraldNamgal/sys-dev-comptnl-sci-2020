#!/usr/bin/env python3

class Animal:

    # a class attribute of the valid species in our universe
    valid_species = {
        'cat',
        'dog',
        'duck',
        'elf',
        'goblin',
        'horse',
        'human',
        'mermaid',
        'nightingale',
        'pig',
        'swan',
        'wolf'
    }

    def __init__(self, name, species):
        self.name = name
        self._species = species     # Non-user-facing attribute (has underscore)

    def __repr__(self):
        return f'{self.name} ({self._species})'

    @property                       # Allows user to directly 'get' species
    def species(self):
        return self._species

    @species.setter                 # Allows user to directly 'set' species
    def species(self, into):
        assert into in Animal.valid_species,\
            Exception(f'invalid species: {into}')
        self._species = into


# TODO: Debugging (erase / comment out later, i.e, no demo needed?)
# dog = Animal('Fido', 'dog')
# print(dog.species)
# dog.species = 'cat'
# print(dog.species)
# dog.species = 'TheThing'
# print(dog.species)
