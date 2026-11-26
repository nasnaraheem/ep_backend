from django.db import models
from accounts.models import User
from django.utils.text import slugify

# Create your models here.
class Assessment(models.Model):
    title=models.CharField(max_length=200)
    batch=models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )
    exam_date=models.DateField()
    duration=models.IntegerField()
    start_time=models.TimeField()
    end_time=models.TimeField(null=True)
    trainer=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


