# test_project.py

import unittest
from habit_tracker import HabitTracker
from analysis import HabitAnalysis

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = HabitTracker()
    
    def tearDown(self):
        self.tracker.client.drop_database("habit_tracker")
    
    def test_add_habit(self):
        self.tracker.add_habit("Exercise", "Daily exercise")
        self.assertEqual(self.tracker.collection.count_documents({}), 1)
    
    def test_mark_completed(self):
        self.tracker.add_habit("Exercise", "Daily exercise")
        self.tracker.mark_completed("Exercise")
        habit = self.tracker.collection.find_one({"name": "Exercise"})
        self.assertTrue(habit["completed"])
    
    def test_export_to_csv(self):
        self.tracker.add_habit("Exercise", "Daily exercise")
        self.tracker.export_to_csv("test_habits.csv")
        # You can add additional assertions or checks to validate the CSV export

class TestHabitAnalysis(unittest.TestCase):
    def setUp(self):
        self.analysis = HabitAnalysis()
    
    def tearDown(self):
        self.analysis.client.drop_database("habit_tracker")
    
    def test_count_completed_habits(self):
        self.analysis.collection.insert_many([
            {"name": "Exercise", "description": "Daily exercise", "completed": True},
            {"name": "Reading", "description": "Read for 30 minutes", "completed": False},
            {"name": "Meditation", "description": "Practice meditation", "completed": True}
        ])
        self.assertEqual(self.analysis.count_completed_habits(), 2)
    
    def test_count_incomplete_habits(self):
        self.analysis.collection.insert_many([
            {"name": "Exercise", "description": "Daily exercise", "completed": True},
            {"name": "Reading", "description": "Read for 30 minutes", "completed": False},
            {"name": "Meditation", "description": "Practice meditation", "completed": True}
        ])
        self.assertEqual(self.analysis.count_incomplete_habits(), 1)

if __name__ == "__main__":
    unittest.main()
