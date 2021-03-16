from django.db import models

# Create your models here.


class Task(models.Model):
    content = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ['-date_created']
