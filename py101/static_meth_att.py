class Student:

    _staticval = -1
    
    @classmethod
    def myclassmethod(x):
        print(x._staticval)
        
        
    @staticmethod
    def mystaticmethod():
        print(Student._staticval)
        
    def my_method(self):
        print(Student._staticval)
        
        
 
Student.myclassmethod()
Student.mystaticmethod()
Student.my_method()

s = Student()

s.myclassmethod()
s.mystaticmethod()
s.my_method()



     