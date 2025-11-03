class A:
    def greet(self):
        print("Hello from class A")

class B:
    def greet(self):
        print("Hello from class B")

class C(A, B):  
    pass

obj = C()
obj.greet() 

# Question Explanation:
# Class A is called because A is listed at first.
