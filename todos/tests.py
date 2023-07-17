from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo

# Create your tests here.
class TodosTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title="read the book",
            body="django apis",
        )
    
    def test_model_content(self):
        task = self.todo
        self.assertEqual(task.title, "read the book"),
        self.assertEqual(task.body, "django apis"),
        self.assertEqual(str(task), "read the book"),

class TodoAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.task = Todo.objects.create(
            title="read the book",
            body="django apis",
        )
        cls.task1 = Todo.objects.create(
            title="study js",
            body="from elzero web school",
        )
    
    def test_list_api(self):
        response_object = self.client.get(reverse("todo_api:todo_list"))
        self.assertEqual(response_object.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 2)
        self.assertContains(response_object, self.task)
        self.assertContains(response_object, self.task1.body)
        self.assertContains(response_object, "read the book")
    
    def test_retrieve_api(self):
        response_object = self.client.get(reverse("todo_api:todo_detail", kwargs={"pk":2}))
        self.assertEqual(response_object.status_code, status.HTTP_200_OK)
        self.assertContains(response_object, "from elzero web school")