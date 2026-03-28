"""
abstraction is the process of hiding the complex implementation
details of a system and showing only the essential features or functionality to the user.
"""

from abc import ABC,abstractmethod

class Bike: # abstract base class

    @abstractmethod
    def transmission(self): pass # abstract method

    @abstractmethod
    def start(self): pass # abstract method

# in abstraction Pulsar should give definition for all methods inherited from Bike abstarct base class otherwise error

class Pulsar(Bike):

    def transmission(self): 

        print("pulsar transmission")


    def start(self): 

        print("start method")

pulsar_inst = Pulsar()

pulsar_inst.transmission()
pulsar_inst.start()