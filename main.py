from pyscript import display, document


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello! My name is {self.name}. My section is {self.section}, and this is my favorite subject: {self.favorite_subject}!"

classmates = [
    Classmate("Joe Abayon", "Emerald", "English"),
    Classmate("Rin Antes", "Emerald", "Sir Temp"),
    Classmate("Cait Apostol", "Emerald", "English"),
    Classmate("Kyla Banaag", "Emerald", "English"),
    Classmate("Do I make myself Clairo Casal", "Emerald", "Sir Marcaroni")
]
def show_classmates(event):
    document.getElementById("output").innerHTML = "" 
    display(" Classmate List:", target="output")
    for c in classmates:
        display(c.introduce(), target="output")


def add_classmate(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    if name and section and subject:
        new_classmate = Classmate(name, section, subject)
        classmates.append(new_classmate)
        display(f"{name} has been added!!", target="output")
    else:
        display("Please answer all.", target="output")
