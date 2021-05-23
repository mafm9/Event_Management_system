import json
import datetime as dt
import os
import random
import mysql.connector

cnx = mysql.connector.connect(user=os.getenv('db_user'), database='events')


class event:
    def __init__(self, name, date_of_event, event_type) -> None:
        self.name = name
        self.date_of_event = dt.datetime.strptime(date_of_event, "%m-%d-%Y").strftime('%Y-%m-%d')
        self.event_type = event_type

    def __str__(self) -> str:
        return f"date_of_event: {self.date_of_event}\n" \
               f"name: {self.name}\n" \
               f"event: {self.event_type}\n" \
               f"gift idea: {gift(self.event_type)}\n"


def new_event_dict() -> dict:
    date_of_event = input("please enter date of event: ")
    while not validate_date(date_of_event):
        date_of_event = input("Date format incorrect please input date as MM-DD-YYYY: ")
    date_of_event = dt.datetime.strptime(date_of_event, "%m-%d-%Y").strftime('%Y-%m-%d')
    name = input("Please enter who's event it is: ").title()
    event_type = input("Please enter what the event is: ").capitalize()
    return {"date_of_event": date_of_event,
            "name": name,
            "type_of_event": event_type
            }


def new_event_obj():
    date_of_event = input("please enter date of event: ")
    while not validate_date(date_of_event):
        date_of_event = input("Date format incorrect please input date as MM-DD-YYYY: ")
    name = input("Please enter who's event it is: ")
    type_of_event = input("Please enter what the event is: ")
    return event(name, date_of_event, type_of_event)


def validate_date(event_date) -> bool:
    try:
        dt.datetime.strptime(event_date, "%m-%d-%Y")
        return True
    except ValueError:
        return False


def event_date_formatting(event_date) -> str:
    return dt.datetime.strptime(event_date, "%m-%d-%Y").strftime('%Y-%m-%d')


def add():
    cursor = cnx.cursor(buffered=True)
    new_entry = new_event_obj()
    insert = ("INSERT INTO event(name,eventDate,eventType)"
              "Values(%s,%s,%s)")
    cursor.execute(insert, (new_entry.name, new_entry.date_of_event, new_entry.event_type))
    cnx.commit()


def edit():
    cursor_select = cnx.cursor(buffered=True)
    cursor_update = cnx.cursor(buffered=True)
    select = ("SELECT eventid From event "
              "WHERE name = %s AND eventDate = %s AND eventType = %s")
    print("Input event you want to change: ")
    current_event = new_event_obj()
    cursor_select.execute(select, (current_event.name, current_event.date_of_event, current_event.event_type))
    eventid = cursor_select.fetchone()
    if eventid:
        eventid = eventid[0]
        print("1.change date")
        print("2.change name")
        print("3.change type of event")
        x = input("Select option: ")
        if x == "1":
            new_date = input("When will the date take place: ")
            new_date = event_date_formatting(new_date)
            update = ("UPDATE event SET eventDate = %s "
                      "WHERE eventid = %s")
            cursor_update.execute(update, (new_date, eventid))
            cnx.commit()
        elif x == "2":
            new_name = input("enter a new name for the event: ").title()
            update = ("UPDATE event SET name = %s "
                      "WHERE eventid = %s")
            cursor_update.execute(update, (new_name, eventid))
            cnx.commit()

        elif x == "3":
            new_event_type = input("what are you celebrating instead: ")
            update = ("UPDATE event SET eventType = %s "
                      "WHERE eventid = %s")
            cursor_update.execute(update, (new_event_type, eventid))
            cnx.commit()
    else:
        print("please input valid event: ")
        edit()


def delete():
    delete_event = new_event_obj()
    cursor_select = cnx.cursor(buffered=True)
    cursor_delete = cnx.cursor(buffered=True)
    select = ("SELECT eventid From event "
              "WHERE name = %s AND eventDate = %s AND eventType = %s")
    cursor_select.execute(select, (delete_event.name, delete_event.date_of_event, delete_event.event_type))
    eventid = cursor_select.fetchone()
    eventid = eventid[0]
    delete_event = ("DELETE FROM event "
                    "WHERE eventId = %s")
    cursor_delete.execute(delete_event, (eventid,))
    cnx.commit()


def name_search():
    name = input("Please enter name you're looking for: ").title()
    cursor = cnx.cursor(buffered=True)
    select = ("SELECT * from event "
              "Where name = %s")
    cursor.execute(select, (name,))
    events = cursor.fetchall()
    for values in events:
        temp = event(values[0], dt.datetime.strftime(values[1], "%m-%d-%Y"), values[2])
        print(temp)


def event_search():
    event_type = input("Please enter event you're looking for: ").capitalize()
    cursor = cnx.cursor(buffered=True)
    select = ("SELECT * from event "
              "Where eventType = %s")
    cursor.execute(select, (event_type,))
    events = cursor.fetchall()
    for values in events:
        temp = event(values[0], dt.datetime.strftime(values[1], "%m-%d-%Y"), values[2])
        print(temp)


def upcoming():
    today = dt.datetime.now().date()
    events = []
    cursor = cnx.cursor(buffered=True)
    select_dates = "SELECT * from event"
    cursor.execute(select_dates)
    dates = cursor.fetchall()
    for date in dates:
        temp = event(date[0], dt.datetime.strftime(date[1], "%m-%d-%Y"), date[2])
        event_date = dt.datetime.strptime(str(date[1]), "%Y-%m-%d").date()
        days_away = (event_date - today).days
        if 0 < days_away < 7:
            events.append(temp)
    if events:
        print("The following are events coming up within the week:")
        for item in events:
            print(item)


def notification():
    today = dt.datetime.now().date()
    events = []
    cursor = cnx.cursor(buffered=True)
    select_dates = "SELECT * from event"
    cursor.execute(select_dates)
    dates = cursor.fetchall()
    for date in dates:
        temp = event(date[0], dt.datetime.strftime(date[1], "%m-%d-%Y"), date[2])
        event_date = dt.datetime.strptime(str(date[1]), "%Y-%m-%d").date()
        days_away = (event_date - today).days
        if 0 < days_away < 3:
            events.append(temp)
    if events:
        print("The following are events coming up within the next few days.")
        for item in events:
            print(item)


def gift(type_of_event):
    cursor = cnx.cursor(buffered=True)
    select_events = "SELECT DISTINCT eventType from gifts"
    cursor.execute(select_events)
    events = cursor.fetchall()
    if type_of_event not in events:
        type_of_event = "Misc"
    select_gifts = ("SELECT giftIdea FROM gifts "
                    "WHERE eventType = %s")
    cursor.execute(select_gifts, (type_of_event,))
    gifts = cursor.fetchall()
    random.shuffle(gifts)
    return gifts.pop()[0]
