from django.db import models
from django.db import models

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name}-{self.subject}"

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'
