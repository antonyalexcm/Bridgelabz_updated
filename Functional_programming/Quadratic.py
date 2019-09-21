
from math import sqrt

def quadratic(a,b,c):
    delta = b*b - 4*a*c 

    if delta >= 0:
        root1 = (-b + sqrt(delta))/(2*a)
        root2 = (-b - sqrt(delta))/(2*a)

        return root1, root2

    elif delta < 0 :
        print("\n Complex number solution!!!!")
        

if __name__ == "__main__":
    print("The equation is in the form ax^2 + bx + c !!!")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    sol = quadratic(a,b,c)
    print("\nThe roots of the equation are:", sol)
