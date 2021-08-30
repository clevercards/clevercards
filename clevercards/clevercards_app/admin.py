from abc import abstractmethod
from django.contrib import admin
from .models import Subject


admin.site.register(Subject)