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

from pyscript import display, document
import matplotlib.pyplot as plt

attendance = {}

def add_data(event):
    day = document.getElementById("day").value
    absence = document.getElementById("absence").value

    log = document.getElementById("log")

    if absence == "":
        log.innerHTML = "⚠️ Please enter a number"
        return

    attendance[day] = int(absence)

    log.innerHTML = f"✅ Added: {day} - {absence} absences"


def show_graph(event):
    graph = document.getElementById("graph")

    if len(attendance) == 0:
        document.getElementById("log").innerHTML = "⚠️ No data to display"
        return
        
    graph.innerHTML = ""

    days = list(attendance.keys())
    absences = list(attendance.values())

    plt.figure()
    plt.plot(days, absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Days")
    plt.ylabel("Number of Absences")
    plt.grid()

    display(plt, target="graph")
