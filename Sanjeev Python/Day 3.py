class wipro:
    def __init__(self,x,y):
        self.a=x;self.b=y
    def display(self):
        print 'Display'
    def __del__(self):
        print 'Destructed'

m=wipro(1,2)
n=wipro(3,4)
m.display()
print m.a,m.b
del m


class wiproltd:
    def __init__(self):
        print "Base Constructor"
    def display(self):
        print 'Display paresnt'

class wiprodop(wiproltd):
    def __init__(self):
        print "Child Constructor"
    def display1(self):
        print 'Display child'

ob=wiprodop()
ob.display1()
ob.display()



class Wiproltd(object):
    @classmethod
    def display1(self):
        print 'Display paresnt'

class Wiprodop(Wiproltd):
    @classmethod
    def display1(self):
        super(wiprodop,self).display1()
        print 'Display child'

ob=wiprodop()
ob.display1()
print Wiprodop.__mro__


