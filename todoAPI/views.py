from django.views import View
from django.http import JsonResponse
from .models import TodoItem

class TaskView(View):
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


    
