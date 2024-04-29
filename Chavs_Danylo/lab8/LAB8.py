class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}")


class Child1(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")


class Child2(Parent):
    def __init__(self, name, hobby):
        super().__init__(name)
        self.hobby = hobby

    def describe_hobby(self):
        print(f"My hobby is {self.hobby}.")


class Child3(Child1):
    def __init__(self, name, age, friend):
        super().__init__(name, age)
        self.friend = friend

    def introduce_and_greet_friend(self):
        print(f"My name is {self.name}, I'm {self.age} years old, and my friend is {self.friend.name}.")

    def describe_friend_hobby(self):
        print(f"My friend's hobby is {self.friend.hobby}.")



parent = Parent("John")
child1 = Child1("Alice", 25)
child2 = Child2("Bob", "Painting")
child3 = Child3("Carol", 30, child2)


parent.greet() 
child1.introduce()  
child2.describe_hobby()  
child3.introduce_and_greet_friend()  
child3.describe_friend_hobby()  
