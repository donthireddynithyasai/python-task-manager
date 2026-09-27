import unittest
import task_manager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        task_manager.tasks.clear()

    def test_add_task(self):
        task_manager.add_task("Study Python")
        self.assertIn("Study Python", task_manager.tasks)

    def test_view_tasks_empty(self):
        task_manager.view_tasks()
        self.assertEqual(task_manager.tasks, [])

    def test_delete_task(self):
        task_manager.add_task("Study Python")
        task_manager.delete_task(1)
        self.assertEqual(task_manager.tasks, [])

    def test_add_multiple_tasks(self):
        task_manager.add_task("Task 1")
        task_manager.add_task("Task 2")
        self.assertEqual(len(task_manager.tasks), 2)

if __name__ == "__main__":
    unittest.main()