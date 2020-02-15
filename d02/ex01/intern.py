#!/usr/bin/env python3

class Intern:
    def __init__(self, n="My name? I’m nobody, an intern, I have no name." ):
        self.Name = n

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

 



if __name__ == "__main__":
    i1 = Intern()
    Mark = Intern("Mark")
    print(i1)
    print(Mark)
    print(Mark.make_coffee())
    try:
        print(i1.work())
    except Exception as e:
        print(e)
