#!/usr/bin/env python3


class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f'name: \"{self.name}\"\n'+'price: %.2f' % round(self.price, 2)+f'\ndescription: \"{self.description()}\"'


class EmptyCup(HotBeverage):
    def __init__(self):
        self.name = 'empty cup'
        self.price = 0.90

    def description(self):
        return "An empty cup?! Gimme my money back!"


class Coffee(HotBeverage):
    def __init__(self):
        self.price = 0.40
        self.name = "coffee"

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        self.price = 0.30
        self.name = "tea"


class Chocolate(HotBeverage):
    def __init__(self):
        self.price = 0.50
        self.name = "coffee"

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        self.price = 0.45
        self.name = "cappuccino"

    def description(self):
        return "Un po’ di Italia nella sua tazza!"

