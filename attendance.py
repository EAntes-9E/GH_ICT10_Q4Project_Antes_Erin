from pyscript import display, document
import matplotlib.pyplot as plt

attendance = {}

def add_data(event):
    day = document.getElementById("day").value
    absence = document.getElementById("absence").value

    log = document.getElementById("log")

    if absence == "":
        log.innerHTML = "Please enter a number"
        return

    attendance[day] = int(absence)

    log.innerHTML = f"Added: {day} - {absence} absences"


def show_graph(event):
    graph = document.getElementById("graph")

    if len(attendance) == 0:
        document.getElementById("log").innerHTML = "No data to display"
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
