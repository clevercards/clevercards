from abc import abstractmethod
from django.contrib import admin
from .models import Quiz


admin.site.register(Quiz)