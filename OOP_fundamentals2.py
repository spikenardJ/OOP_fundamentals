# Question 1: City Infrastructure Management System

# Task 2: Event Management System Enhancement

from termcolor import colored

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        self.participants = []

    def add_participant(self, participant_name):
        self.participants.append(participant_name)
        self.participant_count += 1

    def display_event(self):
        print(colored(f"\nEvent Name: {self.name} \nEvent Date: {self.date} \nTotal Participants: {self.participant_count}", "white", attrs=["bold"]))
        for participant in self.participants:
            print(colored(f"{participant}", "light_cyan"))

events = {}


def get_participant_count(participant_count):
    return participant_count

while True:
    action = input("\nEnter action for Event (Add, Register, Display, Exit): ").title()
    if action == "Exit":
        break
    try:
        if action == "Add":
            name = input("Enter event name: ").title()
            date = input("Enter event date: ")
            events[name] = Event(name, date)
        elif action == "Register":
            event_name = input("Enter event name: ").title()
            participant_name = input("Enter participant name: ").title()
            if event_name in events:
                events[event_name].add_participant(participant_name)
            else:
                print("Event not found.")
        elif action == "Display":
            for event in events.values():
                event.display_event()


    except Exception as e:
        print(f"An error occured: {e}")

print("\nEvent Management System Enhancement closed.")