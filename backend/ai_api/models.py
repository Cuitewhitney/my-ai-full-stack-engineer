from django.db import models

class Enhancement(models.Model):
    original = models.TextField()
    enhanced = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original[:50]
