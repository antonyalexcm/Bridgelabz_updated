"""def Recursion(Num):
    print("\n",Num)
    if(Num == 0):
        return
    Recursion(Num-1)
    print("Inner-P",Num+10)

if __name__ =="__main__":
    Recursion(10)"""

'''def fahrenheit(T_in_celsius):
    """ returns the temperature in degrees Fahrenheit """
    return (T_in_celsius * 9 / 5) + 32

for t in (22, 25, 27, 29):
    print(t, ": ", fahrenheit(t))'''

'''def Hello(name='everybody'):
     
     print("Hello " + name + "!")
     """name='everybody'"""
     #""" Greets a person """

Hello('Peter')
Hello('D')
Hello()
print(Hello.__doc__)'''

'''def sumsub(a, b, c=0, d=0):
    return a - b + c - d

print(sumsub(12,4))
print(sumsub(42,c=2,d=10))

print(sumsub(42,15,2,10))'''

'''a = '25'
print(type(a))'''

'''o1 = type('X', (object,), dict(a='Foo', b=12)) 
  
print(type(o1)) 
print(vars(o1)) 
  
class test: 
    a = 'Foo'
    b = 12
    
o2 = type('Y', (test,), dict(a='Foo', b=12)) 
print(type(o2)) 
print(vars(o2))'''

class Test: 
    a = 5
    
TestInstance = Test() 
  
print(isinstance(TestInstance, class)) 
print(isinstance(TestInstance, (list, tuple))) 
print(isinstance(TestInstance, (list, tuple, Test))) 