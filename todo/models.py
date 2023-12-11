from django.db import models

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

    title = models.CharField(max_length=255)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default=MEDIUM_PRIORITY)

    def __str__(self) -> str:
        return self.title

