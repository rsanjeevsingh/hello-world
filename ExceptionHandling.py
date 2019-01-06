try:
    x=input("x=")
    y=input("y=")
    res=x/y
    print res
except ZeroDivisionError,e:
    print 'Arthemetic Excception',e,type(e)
except TypeError,e:
    print 'Type Error',e,type(e)
except NameError,e:
    print 'Name Error',e,type(e)

except Exception, e:
    print 'Any other error'

else:
        print "I execute only when error is not occured"

finally:
        print "I get executed irrespective of error thrown or not"
