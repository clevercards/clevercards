from django.contrib import admin
from .models import Question, Answer, Tag

class AnswerInLine(admin.TabularInline):
    model = Answer

class TagInLine(admin.TabularInline):
    model = Tag

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine, TagInLine]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Tag)

# Google about adding inlines on DJANGO!! IMPORTANT