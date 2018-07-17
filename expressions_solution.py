

def expressions(*args, **kwargs):
    for a in args:
	    print("I see positional arg: %s" % a)
    for k,v in kwargs.items():
        print("I see keyword arg: %s with value %r" % (k,v))

expressions("cow", "horse", "sheep", size="small", clay =True)
