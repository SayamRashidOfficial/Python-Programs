# single inheritance:
'''class A:
    def displayA(self):
        print("welcome to AUST A")
class B(A):
    def displayB(self):
        print("welcome to AUST B")

obj = B()
obj.displayA()
obj.displayB()'''


# multiple inheritance:
'''class A:
    def displayA(self):
        print("welcome to AUST A")
class B:
    def displayB(self):
        print("welcome to AUST B")
class C(A , B):
    def displayC(self):
        print("welcome  to AUST C")

obj = C()
obj.displayA()
'''


# multilevel inheritance
'''class A:
    def displayA(self):
        print("welcome to AUST A")
class B(A):
    def displayB(self):
        print("welcome to AUST B")
class C(B):
    def displayC(self):
        print("welcome  to AUST C")

obj = C()
obj.displayA()
'''
# Hierarchical Inheritance:
class A:
    def displayA(self):
        print("welcome to AUST A")
class B(A):
    def displayB(self):
        print("welcome to AUST B")
class C(A):
    def displayC(self):
        print("welcome  to AUST C")

obj1 = B()
obj2 = C()
obj1.displayB()
obj2.displayC()