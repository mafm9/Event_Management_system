import json
import datetime as dt
import os


class event:
    def __init__(self, name, date_of_event, event_type) -> None:
        self.name = name
        self.date_of_event = date_of_event
        self.event_type = event_type

    def __str__(self) -> str:
        return f"date_of_event: {self.date_of_event}\nname: {self.name}\nevent type: {self.event_type}\n"

    @staticmethod
    def new_event_dict() -> dict:
        date_of_event = input("please enter date of event: ")
        while not validate_date(date_of_event):
            date_of_event = input("Date format incorrect please input date as MM-DD-YYYY: ")
        name = input("Please enter who's event it is: ").title()
        event_type = input("Please enter what the event is: ").capitalize()
        return {"date_of_event": date_of_event,
                "name": name,
                "type_of_event": event_type
                }

    @staticmethod
    def new_event_obj():
        date_of_event = input("please enter date of event: ")
        while not validate_date(date_of_event):
            date_of_event = input("Date format incorrect please input date as MM-DD-YYYY: ")
        name = input("Please enter who's event it is: ")
        type_of_event = input("Please enter what the event is: ")
        return event(name, date_of_event, type_of_event)


def validate_date(event_date):
    try:
        dt.datetime.strptime(event_date, "%m-%d-%Y")
        return True
    except ValueError:
        return False


def add() -> None:
    storage = {}
    add = event.new_event_dict()
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


def edit():
    hold = event.new_event_obj()
    with open("data.json", 'r+') as file:
        data = json.load(file)
        print("1.change date")
        print("2.change name")
        print("3.change type of event")
        x = input("Select option: ")
        if x == "1":
            for item in data['events']:
                if item['date_of_event'] == hold.date_of_event \
                        and item['name'] == hold.name \
                        and item['type_of_event'] == hold.event_type:
                    new_date = input("enter new date: ")
                    item['date_of_event'] = new_date
            file.seek(0)
            json.dump(data, file, indent=4)
        if x == "2":
            for item in data['events']:
                if item['date_of_event'] == hold.date_of_event \
                        and item['name'] == hold.name \
                        and item['type_of_event'] == hold.event_type:
                    new_name = input("enter new name: ")
                    item['name'] = new_name
            file.seek(0)
            json.dump(data, file, indent=4)
        if x == "3":
            for item in data['events']:
                if item['type_of_event'] == hold.date_of_event \
                        and item['name'] == hold.name \
                        and item['type_of_event'] == hold.event_type:
                    new_event = input("enter new event type: ")
                    item['type_of_event'] = new_event
            file.seek(0)
            json.dump(data, file, indent=4)


def delete():
    hold = event.new_event_obj()
    with open("data.json", 'r') as file:
        data = json.load(file)
    for index, item in enumerate(data['events']):
        if item['date_of_event'] == hold.date_of_event \
                and item['name'] == hold.name \
                and item['type_of_event'] == hold.event_type:
            data['events'].pop(index)
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


def name_search():
    name = input("Please enter name you're looking for: ")
    with open("data.json", "r") as file:
        data = json.load(file)
    for item in data['events']:
        temp = event(item['name'], item['date_of_event'], item['type_of_event'])
        if item['name'] == name:
            print(temp)


def event_search():
    event_type = input("Please enter name you're looking for: ")
    with open("data.json", "r") as file:
        data = json.load(file)
    for item in data['events']:
        temp = event(item['name'], item['date_of_event'], item['type_of_event'])
        if item['type_of_event'] == event_type:
            print(temp)


def upcoming():
    today = dt.datetime.now().date()
    events = []
    with open("data.json", "r") as file:
        data = json.load(file)
    for item in data['events']:
        temp = event(item['name'], item['date_of_event'], item['type_of_event'])
        event_date = dt.datetime.strptime(item['date_of_event'], "%m-%d-%Y").date()
        days_away = (event_date - today).days
        if 0 < days_away <= 7:
            events.append(temp)
    if events:
        print("The following are events coming up within the week:")
        for item in events:
            print(item)


def notification():
    today = dt.datetime.now().date()
    notifications = []
    with open("data.json", "r") as file:
        data = json.load(file)
    for item in data['events']:
        temp = event(item['name'], item['date_of_event'], item['type_of_event'])
        event_date = dt.datetime.strptime(item['date_of_event'], "%m-%d-%Y").date()
        days_away = (event_date - today).days
        if 0 < days_away <= 2:
            notifications.append(temp)
    if notifications:
        print("The following events are coming up soon:")
        for item in notifications:
            print(item)

def cleanup():
    today = dt.datetime.now().date()
    deletion = []
    with open("data.json", "r") as file:
        data = json.load(file)
    for item in data['events']:
        temp = event(item['name'], item['date_of_event'], item['type_of_event'])
        event_date = dt.datetime.strptime(item['date_of_event'], "%m-%d-%Y").date()
        days_away = (event_date - today).days
        if 0 < days_away <= 2:
            deletion.append(temp)


def gift(self, e):
    pass
