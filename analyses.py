# analysis.py

from pymongo import MongoClient

class HabitAnalysis:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["habit_tracker"]
        self.collection = self.db["habits"]
    
    def count_completed_habits(self):
        query = {"completed": True}
        return self.collection.count_documents(query)
    
    def count_incomplete_habits(self):
        query = {"completed": False}
        return self.collection.count_documents(query)
