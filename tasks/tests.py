from django.test import TestCase
from django.urls import reverse
from .models import Task, Label
from django.contrib.auth.models import User


class TaskLabelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
            )

    def test_task_list_view(self):
        self.client.login(username='testuser', password='password123')
        Task.objects.create(
            title='Test Task',
            description='This is a test task',
            owner=self.user)
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_create_task_view(self):
        self.client.login(username='testuser', password='password123')
        data = {
            'title': 'New Task',
            'description': 'This is a new task'
        }
        response = self.client.post(reverse('create_task'), data=data)
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_update_task_view(self):
        self.client.login(username='testuser', password='password123')
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            owner=self.user
            )
        data = {
            'title': 'Updated Task',
            'description': 'This is an updated task'
        }
        response = self.client.post(reverse(
            'update_task',
            args=[task.pk]),
            data=data
            )
        self.assertRedirects(response, reverse('task_list'))
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task')
        self.assertEqual(task.description, 'This is an updated task')

    def test_delete_task_view(self):
        self.client.login(username='testuser', password='password123')
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            owner=self.user
            )
        response = self.client.post(reverse('delete_task', args=[task.pk]))
        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_create_label_view(self):
        self.client.login(username='testuser', password='password123')
        data = {'name': 'New Label'}
        response = self.client.post(reverse('create_label'), data)
        self.assertTrue(Label.objects.filter(name='New Label').exists())
        self.assertEqual(response.status_code, 302)

    def test_update_label_view(self):
        label = Label.objects.create(name='Label', owner=self.user)
        self.client.login(username='testuser', password='password123')
        data = {'name': 'Updated Label'}
        response = self.client.post(reverse(
            'update_label',
            kwargs={'pk': label.pk}),
            data
            )
        label.refresh_from_db()
        self.assertEqual(label.name, 'Updated Label')
        self.assertEqual(response.status_code, 302)

    def test_delete_label_view(self):
        label = Label.objects.create(name='Label', owner=self.user)
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse(
            'delete_label',
            kwargs={'pk': label.pk}
            ))
        self.assertFalse(Label.objects.filter(name='Label').exists())
        self.assertEqual(response.status_code, 302)
