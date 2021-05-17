import os.path

import event
import json
import datetime


def options() -> None:
    print("1. add a new event")
    print("2. edit an existing event")
    print("3. delete an existing event")
    print("4. search for an event by name")
    print("5. search for an event by event type")
    print("6. exit")


event.eventManagement.upcoming()
x = ""
storage = {}
while x != "6":
    options()
    x = input("Please select an option ")
    if x == "1":
        add = event.eventManagement.add()
        if os.path.getsize('data.json') != 0:
            with open('data.json', 'r+') as outfile:
                hold = json.load(outfile)
                hold['events'].append(add)
                outfile.seek(0)
                json.dump(hold, outfile, indent=4)
        else:
            with open('data.json', 'w') as outfile:
                storage["events"] = []
                storage['events'].append(add)
                json.dump(storage, outfile, indent=4)

    if x == "2":
        event.eventManagement.edit()

    if x == "3":
        event.eventManagement.delete()

    if x == "4":
        event.eventManagement.name_search()

    if x == "5":
        event.eventManagement.event_search()
