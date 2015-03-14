def log(func):
    def wrapper(*arge,**kw):
        print 'call %s():'%func.__name__
        return func(*arge,**kw)
	return wrapper
	
@log
def now():
    print '2015.3.8'

print  now()