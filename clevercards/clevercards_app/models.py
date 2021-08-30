from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=120)

    def __str__(self):
        return str(self.subject)

    def get_questions(self):
        return self.question_set.all()