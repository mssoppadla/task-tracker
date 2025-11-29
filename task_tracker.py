class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = int(priority)
        
    def __str__(self):
        return f"[priority {self.priority}] {self.name}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, name, priority):
        task = Task(name, priority)
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority)
                
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}") 
    def remove_task(self, index):
        self.tasks.pop(index)
         
def print_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
def main():
    manager = TaskManager()
    
    while True:
        print_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter task name: ")
            priority = input("Enter task priority (higher number = higher priority): ")
            try:
                manager.add_task(name, priority)
                print("Task added.")
            except ValueError:
                print("Priority must be a valid integer.")
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: ")) - 1
                manager.remove_task(index)
                print("Task removed.")
            except (ValueError, IndexError):
                print("Please enter a valid task number.")
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()