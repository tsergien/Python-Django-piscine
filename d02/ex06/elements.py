#!/usr/bin/env python3

from elem import Text, Elem


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super(Html, self).__init__('html', attr, content, 'double')
      
class Head(Elem):
    def __init__(self, content=None, attr={}):
        super(Head, self).__init__('head', attr, content, 'double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super(Body, self).__init__('body', attr, content, 'double')

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super(Title, self).__init__('title', attr, content, 'double')

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super(Meta, self).__init__('meta', attr, content, 'double')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super(Img, self).__init__('img', attr, content, 'simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super(Table, self).__init__('table', attr, content, '')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super(Th, self).__init__('th', attr, content, 'double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super(Tr, self).__init__('tr', attr, content, 'double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super(Td, self).__init__('td', attr, content, 'double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super(Ul, self).__init__('ul', attr, content, 'double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super(Ol, self).__init__('ol', attr, content, 'double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super(Li, self).__init__('li', attr, content, 'double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super(H1, self).__init__('h1', attr, content, 'double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super(H2, self).__init__('h2', attr, content, 'double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        super(P, self).__init__('p', attr, content, 'double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super(Div, self).__init__('div', attr, content, 'double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super(Span, self).__init__('span', attr, content, 'double')

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super(Hr, self).__init__('hr', attr, content, 'simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super(Br, self).__init__('br', attr, content, 'simple')



if __name__ == "__main__":
    print(Html(\
        [\
            Head([Title([Text("Hello ground!")])]), \
            Body( [ H1([Text("Oh no, not again!")]), \
                Img([], {'src':"http://i.imgur.com/pfp3T.jpg"}) ] )\
        ] \
        ))

    
    f = open('my.html', 'w')
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
        
    f.write(Text(obj))
    f.close()
