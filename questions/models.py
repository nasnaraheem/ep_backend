from django.db import models
from assessment.models import Assessment
from django.utils.text import slugify


# Create your models here.
class Questions(models.Model):

    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    assesment=models.ForeignKey(Assessment,on_delete=models.CASCADE)
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )
    order = models.PositiveIntegerField(null= True)
    sample_input=models.CharField(max_length=200,null=True)
    sample_output=models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        question_instance = Questions.objects.filter(assesment=self.assesment).last()

        if question_instance:

            self.order = question_instance.order + 1
        else:
            self.order = 1

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.questions.title} - {self.title}"

    class Meta:
        ordering = ["order"]
        unique_together = ["assesment", "order"]

    
