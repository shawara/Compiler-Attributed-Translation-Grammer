import re
import parseInput

ind = 0


outlist = []
isOk = 1

inp = parseInput.read()
#inp = 'a * b+c/d'
counter = 0

identReg = r'[_a-zA-Z][_a-zA-Z0-9]*'


def genS():
    global counter
    counter += 1
    return 'T' + str(counter)


class OBJ:
    def __init__(self):
        self.first = ''
        self.second = ''


def Expr(expr):
    term = OBJ()
    elist = OBJ()

    Term(term)
    elist.first = term.first
    Elist(elist)
    expr.first = elist.second


def Term(term):
    global isOk
    factor = OBJ()
    tlist = OBJ()

    Factor(factor)
    tlist.first = factor.first
    Tlist(tlist)
    term.first = tlist.second


def Factor(factor):
    global isOk

    global ind
    if re.match(identReg, inp[ind]):
        factor.first = inp[ind]

        ind += 1
    elif inp[ind] == '(':
        ind += 1
        expr = OBJ()
        Expr(expr)

        factor.first = expr.first

        if inp[ind] == ')':
            ind += 1
        else:
            print 'FAILED'
            isOk = 0
    else:
        print 'FAILED', ind, 'Factor'
        isOk = 0


def Elist(elist):
    global isOk

    global ind
    if inp[ind] == '#' or inp[ind] == ')':  # eof  Elist= e
        elist.second = elist.first
    elif inp[ind] == '+' or inp[ind] == '-':  # first of Elist
        if (inp[ind] == '+'):
            op = 'ADD '
        else:
            op = 'SUB '
        ind += 1
        term = OBJ()
        Term(term)

        s = genS()
        # print 'ADD ' + elist.first + ' , ' + term.first + ' , ' + s
        outlist.append(op + elist.first + ' , ' + term.first + ' , ' + s)

        elist2 = OBJ()
        elist2.first = s
        Elist(elist2)
        elist.second = elist2.second

    else:
        print 'FAILED', ind, 'Elist'
        isOk = 0


def Tlist(tlist):
    global isOk

    global ind

    if inp[ind] == '-' or inp[ind] == '+' or inp[ind] == '#' or inp[ind] == ')' or inp[ind] == '(':  # Tlist = ebson
        tlist.second = tlist.first
    elif inp[ind] == '*' or inp[ind] == '/':  # first of Tlisst

        if (inp[ind] == '*'):
            op = 'MULT '
        else:
            op = 'DIV '

        ind += 1
        factor = OBJ()
        Factor(factor)

        s = genS()
        # print 'MULT ' + tlist.first + ' , ' + factor.first + ' , ' + s

        outlist.append(op + tlist.first + ' , ' + factor.first + ' , ' + s)

        tlist2 = OBJ()
        tlist2.first = s
        Tlist(tlist2)
        tlist.second = tlist2.second
    else:
        print 'FAILED', ind, 'Tlist'
        isOk = 0


exp = OBJ()
Expr(exp)

if isOk == 1:
    for i in outlist:
        print i
else:
    print 'Synatx Error'
