
from math import sqrt

def Length(ls1, ls2):
    """Function to calculate the lenght"""
    length = float(sqrt(float(pow((ls2[1]-ls1[1]),2)) +float(pow((ls2[0]-ls1[0]),2))))
    print("The length is:",length)
  
if __name__ == "__main__":
    point_1 = input("Enter the Co-ordinates of 1st point:")

    point_1 = [float(i) for i in point_1.split(',')]

    point_2 = input("Enter the Co-ordinates of 2nd point:")

    point_2 = [float(i) for i in point_2.split(',')]

    print("\n",point_1 )
    print("\n",point_2 )

    Length(point_1,point_2)