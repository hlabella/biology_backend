from django.db import models

# Create your models here.

# question model
class Question(models.Model):

    id = models.CharField(max_length=24, primary_key=True)
    text = models.TextField()
    focos = models.JSONField()  
    image = models.URLField(blank=True, null=True)  # 'imagem' is a URL
    video_resolution = models.URLField(blank=True, null=True)  # 'video_resolucao'
    discipline = models.CharField(max_length=100)  # 'disciplina'
    thematic = models.CharField(max_length=100)  # 'tematica'

    def __str__(self):
        return self.text[:50]  # Display first 50 characters of the question

# choice model
class Choice(models.Model):

    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50] # Display first 50 characters of the alternative
