import json
import datetime as dt


class event:
    def __init__(self, name, date_of_event, event_type) -> None:
        self.name = name
        self.date_of_event = date_of_event
        self.event_type = event_type


class eventManagement:

    @staticmethod
    def add() -> dict:
        date_of_event = input("please enter date of event: ")
        name = input("Please enter who's event it is: ")
        type_of_event = input("Please enter what the event is: ")
        new_event = {"date_of_event": date_of_event,
                     "name": name,
                     "type_of_event": type_of_event
                     }
        return new_event

    @staticmethod
    def edit():
        date_of_event = input("please enter date of event: ")
        name = input("Please enter who's event it is: ")
        type_of_event = input("Please enter what the event is: ")
        hold = event(name, date_of_event, type_of_event)
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

    @staticmethod
    def delete():
        date_of_event = input("please enter date of event: ")
        name = input("Please enter who's event it is: ")
        type_of_event = input("Please enter what the event is: ")
        hold = event(name, date_of_event, type_of_event)
        with open("data.json", 'r') as file:
            data = json.load(file)
        for index, item in enumerate(data['events']):
            if item['date_of_event'] == hold.date_of_event \
                    and item['name'] == hold.name \
                    and item['type_of_event'] == hold.event_type:
                data['events'].pop(index)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def name_search():
        name = input("Please enter name you're looking for: ")
        with open("data.json", "r") as file:
            data = json.load(file)
        for item in data['events']:
            if item['name'] == name:
                print(item)

    @staticmethod
    def event_search():
        event_type = input("Please enter name you're looking for: ")
        with open("data.json", "r") as file:
            data = json.load(file)
        for item in data['events']:
            if item['type_of_event'] == event_type:
                print(item)

    @staticmethod
    def upcoming():
        today = dt.datetime.now().date()
        with open("data.json", "r") as file:
            data = json.load(file)
        for item in data['events']:
            event_date = dt.datetime.strptime(item['date_of_event'], "%m-%d-%Y").date()
            days_away = (event_date - today).days
            if 0 < days_away <= 7:
                print(item)

    def notification(self, e):
        pass

    def gift(self, e):
        pass
