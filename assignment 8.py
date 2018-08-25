Question 1
class circle:
    def area(self):
        return(3.14*r*r)
    def circumference(self):
        return(2*3.14*r)
r=int(input("enter radius"))
c=circle()
print("area is ", c.area())
print("circumference is",c.circumference())

#Question 2
class student:
    def __init__(self):
        self.name=input("enter name")
        self.roll=int(input("enter rollno"))
    def setAge(self):
        self.age=int(input("enter age"))
    def setMarks(self):
        self.marks=int(input("enter marks"))
    def display(self):
        print("name:",self.name,"\n","roll_no:",self.roll,"\n","age:",self.age,"\n","marks:",self.marks)
s=student()
s.setAge()
s.setMarks()
s.display()

#Question 3
class temp:
    def convertFahrenheit(self):
        self.c=int(input("enter temperature in celsius "))
        return((9/5)*self.c+32)
    def convertCelsius(self):
        self.f=int(input("enter temperature in fahrenheit "))
        return((self.f-32)*5/9)
t=temp()
print(t.convertFahrenheit())
print(t.convertCelsius())

#Question 4
class MovieDetails:
    def __init__(self):
        self.artist_name=input("enter artist name ")
        self.year=int(input("enter year "))
        self.rating=int(input("enter ratings out of 5 "))
    def add(self):
        self.movie_name=input("enter movie name ")
        self.collection=int(input("enter total collection "))
    def display(self):
        print(self.movie_name)
        print(self.artist_name)
        print(self.year)
        print(self.rating)
        print(self.collection)
m=MovieDetails()
m.add()
m.display()

#Question 5
class Animal:
    def animal_attribute(self):
        return("The Tiger")
class Tiger(Animal):
    pass
t=Tiger()
print(t.animal_attribute())

#Question 6
'''output is :
A B'''

#Question 7
class shape:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return(self.length*self.breadth)
    def area1(self):
        return(self.length*self.length)
class rectangle(shape):
    pass
class square(shape):
    pass
l=int(input("enter length"))
b=int(input("enter breadth"))
r=rectangle(l,b)
s=square(l,l)
print("area of rectangle: ",r.area())
print("area of square: ",s.area1())
