#!/usr/bin/env python3

from elem import Text, Elem
from elements import *

class Page:
    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        if isinstance(self.elem, Html):
            res = '<!DOCTYPE html>'
            res.append(self.elem.__str__())
        return self.elem.__str__()

    @staticmethod
    def is_one_of_a_kind(elem):
        if not isinstance(elem, Elem):
            return False
        for el in elem.content:
            return Page.is_one_of_a_kind(el)
        return True


    def write_to_file(self, filename):
        try:
            f = open(filename, 'w')
            f.write(self.__str__())
        except:
            print(f'Could not open {filename}')
    

    def is_valid(self):
        if not self.is_one_of_a_kind(self.elem):
            print(f'Not instance of right class {type(self.elem)}')
            return False
        for el in self.elem.content:
            if not Page(el).is_valid():
                return False
        if isinstance(self.elem, Html):
            if len(self.elem.content) != 2 or (not isinstance(self.elem.content[0], Head))\
                or (not isinstance(self.elem.content[1], Body)):
                print("Head body problem")
                return False
        if isinstance(self.elem, Head):
            if len(self.elem.content) != 1 or (not isinstance(self.elem.content[0], Title)):
                print(f'title problem : len = {len(self.elem.content)} ')
                return False
        if isinstance(self.elem, Div) or isinstance(self.elem, Body):
            for el in self.elem.content:
                if (not isinstance(el, H1)) or (not isinstance(el, H2)) or (not isinstance(el, Div))\
                    (not isinstance(el, Table)) or (not isinstance(el, Ul)) or (not isinstance(el, Ol))\
                        or (not isinstance(el, Span)) or (not isinstance(el, Text)):
                    print(f'types in div/body')
                    return False
        if isinstance(self.elem, H1) or isinstance(self.elem, H2) or isinstance(self.elem, Li) or \
            isinstance(self.elem, Th) or isinstance(self.elem, Td):
            for el in self.elem.content:
                if not isinstance(el, Text):
                    print(f'text only in {type(self.elem)}')
                    return False
        if isinstance(self.elem, P):
            for el in self.elem.content:
                if not isinstance(el, Text):
                    return False
        if isinstance(self.elem, Span):
            for el in self.elem.content:
                if not isinstance(el, Text) and not isinstance(el, P):
                    print(f'Span can only contain text or p')
                    return False
        if isinstance(self.elem, Ul) or isinstance(self.elem, Ol):
            for el in self.elem.content:
                if not isinstance(el, Li):
                    print(f'Ul or Ol can only contain Li')
                    return False
        if isinstance(self.elem, Tr):
            if len(self.elem.content) != 1 or \
                (not isinstance(self.elem.content[0], Td)  and not isinstance(self.elem.content[0], Th)):
                print(f'Tr can only contain Td or Th')
                return False
        if isinstance(self.elem, Table):
            for el in self.elem.content:
                if not isinstance(self.elem.content, Tr):
                    print(f'Table can only contain Tr')
                    return False
        return True





if __name__ == "__main__":

    valid = Html([ Head([Title([])]), Body([]) ])
    print(f'valid: {Page(valid).is_valid()}\n')
    
    invalid_no_title = Html([Head([]), Body([])])
    print(f'invalid_no_title: {Page(invalid_no_title).is_valid()}\n')

    invalid_order = Html([Body([]), Head([Title([])])])
    print(f'invalid_order: {Page(invalid_order).is_valid()}\n')

    invalid_body_div = Html([Head([]), Body([Body([Title([])])])])
    print(f'invalid_body_div: {Page(invalid_body_div).is_valid()}\n')

    invalid_not_text = Html([Head([Title([]), Body([])])])
    print(f'invalid_: {Page(invalid_body_div).is_valid()}\n')

    table = Table([P([])])
    print(f'table: {Page(table).is_valid()}\n')

    tr = Tr([P([])])
    print(f'Tr: {Page(table).is_valid()}\n')

    ul = Ul([P([])])
    print(f'Ul: {Page(ul).is_valid()}\n')

    ol = Ul([P([])])
    print(f'Ul: {Page(ul).is_valid()}\n')


    obj = Html(\
        [\
            Head( [ 
                Title([Text("Hello ground!")]), \
                Meta([], {'charset':"utf-8"})
                ] ), \
            Body( [ H1([Text("Oh no, not again!"), H2([Text("hey handsome))))")])]), \
                Img([], {'src':"http://i.imgur.com/pfp3T.jpg"}),\
                Table( [Text("My great recipe"),\
                     Tr([Th([Text("Astronomy")]), Th([Text("Defense against dark arts")])]), \
                    Tr( [ Td([Text("95")]), Td([Text("97")]) ] ),\
                    Tr( [ Td([Text("91")]), Td([Text("67")]) ] ),\
                         ] ),\
                Ul( [ Li([Text("carrots")]), Li([Text("pepper")]), Li([Text("salt")]) ] ),\
                Hr([]),\
                Ol( [ Li([Text("cut carrots")]), Li([Text("cut pepper")]), Li([Text("use salt")]) ] ),\
                P([Text("""Let everything happen to you \n\
                    Beauty and terror\n\
                    Just keep going\n\
                    No feeling is final""")]),\
                Br([]),\
                Div([Text("special for div")])
                     ] )\
        ] \
        )
    print(valid)
    my_awesome_page = Page(obj)
    my_awesome_page.write_to_file("awesome.html")
