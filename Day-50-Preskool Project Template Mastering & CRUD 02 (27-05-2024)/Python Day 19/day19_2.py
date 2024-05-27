class MyClass:
    class_var=0
    def __init__(self):
        MyClass.class_var+=1

obj1 = MyClass()
obj2 = MyClass()
print(MyClass.class_var)