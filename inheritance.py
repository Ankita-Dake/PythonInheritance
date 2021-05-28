# single level inheritance
class collage:
    def cmethod(self):
        print("this is collage class")


class student(collage):
    def smethod(self):
        print("this is student class")


s = student()
s.smethod()
s.cmethod()


# multi level inheritence
class books:
    def bmethod1(self):
        print("This is from books class")


class subject(books):
    def smethod2(self):
        print("This if from subject class")


class subject1(subject):
    def ssmethod3(self):
        print("This is from subject1 class")


s = subject1()
s.bmethod1()
s.smethod2()
s.ssmethod3()


# multiple inheritance
class animal:
    def method1(self, name):
        print("animal name is", name)


class dog(animal):
    def method2(self, name):
        print("animal dog name is", name)


class cat(animal):
    def method3(self, name):
        print("animal cat name is", name)


d = dog()
d.method1('peacock')
d.method2('sam')

c = cat()
c.method1('lion')
c.method3('mauuu')


# scope
# local variable
def show():
    x = 20
    y = 20
    print('sum is', x + y)


show()

# global variable
i = 30
j = 40
def func():
    print('sum is', i + j)

func()

# using global keyword
def func1():
    global p,q
    p,q = 10,20

func1()
print('sum is', p + q)

