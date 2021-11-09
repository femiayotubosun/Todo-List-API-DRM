from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase, APIClient
from api.views import TodolistListCreateView, api_root


class ApiTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_api_root_should_expose_todolist_end_points(self) -> None:
        request = self.factory.get("api/")
        response = api_root(request)
        expected = {"todolists": reverse("todolist-list")}
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("todolists", response.data)

    def test_retrieve_todo_list_should_return_empty_list(self) -> None:
        request = self.factory.get(reverse("todolist-list"))
        response = TodolistListCreateView.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual([], response.data)

    def test_create_todo_list_should_return_new_todo_list(self) -> None:
        request = self.factory.post(
            reverse("todolist-list"), data={"name": "Test Todo list"}
        )
        response = TodolistListCreateView.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("name" in response.data)
