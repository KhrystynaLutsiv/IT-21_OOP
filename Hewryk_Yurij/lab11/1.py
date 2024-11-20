import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Person(Prototype):
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Skills: {', '.join(self.skills)}"

if __name__ == "__main__":
    original_person = Person("John", 30, ["Python", "Django"])
    print("Original:", original_person)

    cloned_person = original_person.clone()

    cloned_person.add_skill("JavaScript")
    cloned_person.name = "Mike"

    print("Cloned:", cloned_person)
    print("Original after clone:", original_person)
