from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject
from django.views.generic import ListView

class QuizListView(ListView):
    model = Subject
    template_name = 'quizes/main.html'

def quiz_view(request, pk):
    quiz = Subject.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})

def quiz_data_view(request, pk):
    subject = Subject.objects.get(pk=pk)
    questions = []
    correct_answers = []
    allTags = []
    for q in subject.get_questions():
        answers = []
        for a in q.get_answers():
            if a.correct:
                correct_answers.append(a.text)
            answers.append(a.text)
        questions.append({str(q): answers})
        tags = []
        for t in q.get_tags():
            tags.append(t.text)
        allTags.append(tags)
    return JsonResponse({
        'data': questions,
        'answers': correct_answers,
        'tags': allTags,
        'subject': subject.subject,
    })