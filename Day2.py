#Day 2 - Tuple Program
#Comment 2
#Comment 3

tupleLabel = (10,20,30,40,50)
print tupleLabel

print tupleLabel.index(10)

t1=tuple((10,20,30,40,50)) #2nd way
print t1
#tuple.insert(x)

#Create List
l1=[10,20,30,40,50] #1 - normal way
l2=list([100,200,300,400,500]) #2 - list constructor l2=list([va1,va2..])
l3=list() #3 - Empty list

#Create Tuple
t1=(10,20,30,40,50)
t2=tuple((100,200,300,400,500))
t3=tuple() #3 -Empty tuple - can't make changes
print t2


### Function ####


def functionCall():
        print "Function Call"
        print "EOF", dir()
        functioncall2()

def functioncall2():
        print "2nd function"

print "First line..."
functionCall()
print "Back to Main", dir()




label=lambda signature:expression

res = lambda x,y:x+y #Anonymous Function
print "Executing the main block functions"
a=10
b=20
z=res(a,b)
print z, type(res)
print dir()
