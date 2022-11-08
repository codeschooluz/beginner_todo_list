from django.views import View
from django.http import JsonResponse
from .models import TodoItem

class GetAllTaskView(View):
    def get(self, request):
        """
        Get all tasks

        args:
            request: HTTP request

        returns:  JSON response      
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass

class GetTask(View):
    def get(self, request, id):
        """
        Get a task

        args:
            request: HTTP request
            id: int

        returns:  JSON response      
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass

class CreateTask(View):
    def post(self, request):
        """
        Create a task

        args:
            request: HTTP request
            username: string
            password: string
            task: string
            description: string
        
        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass

class UpdateTask(View):
    def post(self, request, id):
        """
        Update a task

        args:
            request: HTTP request
            id: int
            task: string
            description: string
            status: boolean
        
        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass

class DeleteTask(View):
    def get(self, request, id):
        """
        Delete a task

        args:
            request: HTTP request
            id: int

        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass

class CompleteTask(View):
    def get(self, request, id):
        """
        Complete a task

        args:
            request: HTTP request
            id: int

        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass


class GetCompletedTask(View):
    def get(self, request):
        """
        Get completed tasks

        args:
            request: HTTP request

        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass

class GetIncompleteTask(View):
    def get(self, request):
        """
        Get incomplete tasks

        args:
            request: HTTP request

        returns:  JSON response
        id: int
        task: string
        description: string
        status: boolean
        created_at: datetime
        updated_at: datetime

        """
        pass


       


    
