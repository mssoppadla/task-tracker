import unittest
from task_tracker import Task, TaskManager

class TestTask(unittest.TestCase):
    def test_task_creation_valid(self):
        task = Task("Test task", "5")
        self.assertEqual(task.name, "Test task")
        self.assertEqual(task.priority, 5)
    
    def test_task_creation_invalid_priority(self):
        with self.assertRaises(ValueError):
            Task("Test task", "invalid")
    
    def test_task_str(self):
        task = Task("Test task", "3")
        self.assertEqual(str(task), "[priority 3] Test task")

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
    
    def test_add_task(self):
        self.manager.add_task("Task 1", "5")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].name, "Task 1")
    
    def test_add_multiple_tasks_sorted(self):
        self.manager.add_task("Low priority", "1")
        self.manager.add_task("High priority", "5")
        self.assertEqual(self.manager.tasks[0].priority, 1)
        self.assertEqual(self.manager.tasks[1].priority, 5)
    
    def test_remove_task(self):
        self.manager.add_task("Task 1", "5")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 0)
    
    def test_remove_task_invalid_index(self):
        with self.assertRaises(IndexError):
            self.manager.remove_task(0)

if __name__ == "__main__":
    unittest.main()