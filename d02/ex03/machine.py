#!/usr/bin/env python3

import random
from beverages import HotBeverage, EmptyCup, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.cups = 0
        return

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        self.cups = 0

    def serve(self, drink):
        if self.cups >= 10:
            raise self.BrokenMachineException()
        case = random.random() > 0.5
        self.cups += 1
        if case:
            return drink
        else:
            return EmptyCup()



if __name__ == "__main__":
    Neskafe = CoffeeMachine()
    try:
        print(Neskafe.serve(HotBeverage()))
        print(Neskafe.serve(Coffee()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Chocolate()))
        print(Neskafe.serve(Chocolate()))
        print(Neskafe.serve(Chocolate()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Cappuccino()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Tea()))
    except CoffeeMachine.BrokenMachineException as e:
        print(f'\033[1;31m{e}\033[;0m')
    
    Neskafe.repair()

    try:
        print(Neskafe.serve(HotBeverage()))
        print(Neskafe.serve(Coffee()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Chocolate()))
        print(Neskafe.serve(Chocolate()))
        print(Neskafe.serve(Chocolate()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Cappuccino()))
        print(Neskafe.serve(Tea()))
        print(Neskafe.serve(Tea()))
    except CoffeeMachine.BrokenMachineException as e:
        print(f'\033[1;31m{e}\033[;0m')
