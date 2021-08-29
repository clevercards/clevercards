from django.db import models
from clevercards_app.models import Subject

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    def get_tags(self):
        return self.tag_set.all()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False);
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class Tag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"question: {self.question.text}, tags: {self.text}"