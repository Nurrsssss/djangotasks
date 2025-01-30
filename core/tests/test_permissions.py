from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse

class RoleBasedPermissionsTest(TestCase):

    def setUp(self):
        """Set up test users and API client."""
        self.client = APIClient()
        User = get_user_model()
        
        # Create test users with different roles
        self.admin_user = User.objects.create_user(username='admin', password='adminpass', role='admin')
        self.manager_user = User.objects.create_user(username='manager', password='managerpass', role='manager')
        self.employee_user = User.objects.create_user(username='employee', password='employeepass', role='employee')

    def test_admin_access(self):
        """Test that admin can access user list."""
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('user-list'))  # Ensure 'user-list' is the correct view name
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_manager_access(self):
        """Test that manager can access project list."""
        self.client.login(username='manager', password='managerpass')
        response = self.client.get(reverse('project-list'))  # Ensure 'project-list' is correct
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_employee_access(self):
        """Test that employee can access task list."""
        self.client.login(username='employee', password='employeepass')
        response = self.client.get(reverse('task-list'))  # Ensure 'task-list' is correct
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        #ge,lf.
