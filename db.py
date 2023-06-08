# habit_tracker.py

from pymongo import MongoClient
import csv

class HabitTracker:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["habit_tracker"]
        self.collection = self.db["habits"]
    
    def add_habit(self, name, description):
        habit = {"name": name, "description": description, "completed": False}
        self.collection.insert_one(habit)
    
    def mark_completed(self, name):
        query = {"name": name}
        update = {"$set": {"completed": True}}
        self.collection.update_one(query, update)
    
    def print_habits(self):
        habits = self.collection.find()
        for habit in habits:
            print(f"Name: {habit['name']}, Description: {habit['description']}, Completed: {habit['completed']}")
    
    def export_to_csv(self, filename):
        habits = self.collection.find()
        fieldnames = ["Name", "Description", "Completed"]
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for habit in habits:
                writer.writerow({"Name": habit["name"], "Description": habit["description"], "Completed": habit["completed"]})
