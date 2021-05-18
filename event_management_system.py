import event
from os import system,name

def options() -> None:
    print("1. add a new event")
    print("2. edit an existing event")
    print("3. delete an existing event")
    print("4. search for an event by name")
    print("5. search for an event by event type")
    print("6. show upcoming events")
    print("7. exit")


def enter() -> None:
    input("Press enter to continue")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


print("Welcome to the event management system")
enter()
event.notification()
x = ""
while x != "7":
    options()
    x = input("Please select an option ")
    if x == "1":
        event.add()
        enter()

    if x == "2":
        event.edit()
        enter()

    if x == "3":
        event.delete()
        enter()

    if x == "4":
        event.name_search()
        enter()

    if x == "5":
        event.event_search()
        enter()
    
    if x == "6":
        event.upcoming()
        enter()
    clear()
