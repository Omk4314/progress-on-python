from datetime import date
import re

#Build a task management system with users, projects, tasks, deadlines
class User:
    def __init__(self, name):
        self.name = name
        self.projects = {}

    def __str__(self):
        return f"The User name is {self.name}"

    def __repr__(self):
        return f"User: (name = {self.name})"

    def create_project(self, title, deadline):
        project = Project(title, deadline)
        self.projects[project.title] = project
        return project
    
    def mark_complete(self, project_title):
        project = self.projects[project_title]
        project.completed = True

    def remove_project(self, project_title):
        del self.projects[project_title]
        

    def show_projects(self):
        for project in self.projects.values():
            status = "overdue" if project.is_overdue else "ok"
            print(f"Project title: {project.title} | Deadline: {project.deadline} | Status: {status}")

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if match := re.search(r"^(\w+ ?)$", name, re.IGNORECASE):
            self._name = match.group(1)
        else:
            raise ValueError("Enter Words!")

class Project:
    def __init__(self, title, deadline, completed = False):
        self.title = title
        self.deadline = deadline
        self.completed = completed
        self.tasks = []

    def __str__(self):
        return f"The Project Title is {self.title} and the deadline is {self.deadline}"

    def __repr__(self):
        return f"Project: (title = {self.title}, deadline = {self.deadline}, completed = {self.completed})"

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def is_overdue(self):
        return not self.completed and self.deadline < date.today()

    @property
    def deadline(self):
        return self._deadline
    @deadline.setter
    def deadline(self, deadline):
        if match := re.search(r"^(\d{2})/ ?(\d{2})/ ?(\d{4})$", deadline):
            try:
                self._deadline = date(int(match.group(3)), int(match.group(2)), int(match.group(1)))
            except ValueError:
                print("Day should be from 1 - 31, Month must be from 1-12")
        else:
            raise ValueError("Enter the deadline in dd/mm/yyyy")


        

def main():

    # --- Test User creation and string representation ---
    print("=" * 50)
    print("TEST 1: User Creation")
    print("=" * 50)
    alice = User("Alice")
    print(f"__str__: {alice}")
    print(f"__repr__: {repr(alice)}")
    print()

    # --- Test Project creation via User ---
    print("=" * 50)
    print("TEST 2: Project Creation")
    print("=" * 50)
    website = alice.create_project("Website", "05/06/2026")
    mobile_app = alice.create_project("MobileApp", "01/01/2025")
    print(f"__str__: {website}")
    print(f"__repr__: {repr(website)}")
    print()

    # --- Test Task management ---
    print("=" * 50)
    print("TEST 3: Task Management")
    print("=" * 50)
    website.add_task("Design homepage")
    website.add_task("Setup database")
    website.add_task("Write API")
    print("Tasks in 'Website':")
    website.view_tasks()

    website.remove_task("Setup database")
    print("\nAfter removing 'Setup database':")
    website.view_tasks()
    print()

    # --- Test Overdue Check ---
    print("=" * 50)
    print("TEST 4: Overdue Check")
    print("=" * 50)
    print(f"Website overdue? {website.is_overdue()}")
    print(f"MobileApp overdue? {mobile_app.is_overdue()}")
    print()

    # --- Test Show Projects ---
    print("=" * 50)
    print("TEST 5: Show All Projects")
    print("=" * 50)
    alice.show_projects()
    print()

    # --- Test Mark Complete ---
    print("=" * 50)
    print("TEST 6: Mark Complete")
    print("=" * 50)
    alice.mark_complete("Website")
    print(f"After marking complete: {repr(website)}")
    print(f"Website overdue? {website.is_overdue()}")
    print()

    # --- Test Remove Project ---
    print("=" * 50)
    print("TEST 7: Remove Project")
    print("=" * 50)
    alice.remove_project("MobileApp")
    alice.show_projects()
    print()

    # --- Test Name Validation ---
    print("=" * 50)
    print("TEST 8: Validation")
    print("=" * 50)
    try:
        bad_user = User("Alice123!!!")
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        bad_project = Project("Bad", "not-a-date")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    




if __name__ == "__main__":
    main()