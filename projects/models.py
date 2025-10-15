from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    division_name = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    goal = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[('planned', 'Planned'), ('ongoing', 'Ongoing'), ('completed', 'Completed')],
        default='planned'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
