from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review_text = models.TextField()
    profile_image = models.ImageField(upload_to='reviews/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating} stars"
