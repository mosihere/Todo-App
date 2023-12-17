from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Todo(models.Model):

    LOW_PRIORITY = 'L'
    MEDIUM_PRIORITY = 'M'
    HIGH_PRIORITY = 'H'

    PRIORITY_CHOICES = [
        (LOW_PRIORITY, 'Low'),
        (MEDIUM_PRIORITY, 'Medium'),
        (HIGH_PRIORITY, 'High')
    ]

    IN_PROGRESS_STAUTS = 'I'
    PENDING_STATUS = 'P'
    DONE_STATUS = 'D'

    STATUS_CHOICES = [
        (IN_PROGRESS_STAUTS, 'In Progress'),
        (PENDING_STATUS, 'Done'),
        (DONE_STATUS, 'Pending')
    ]


    title = models.CharField(max_length=255)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=MEDIUM_PRIORITY)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING_STATUS)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title