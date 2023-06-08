# main.py

from habit_tracker import HabitTracker

def main():
    tracker = HabitTracker()
    tracker.add_habit("Exercise", "Daily exercise")
    tracker.add_habit("Reading", "Read for 30 minutes")
    
    tracker.mark_completed("Exercise")
    tracker.mark_completed("Reading")
    
    tracker.print_habits()
    tracker.export_to_csv("habits.csv")

if __name__ == "__main__":
    main()
