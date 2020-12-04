from django.contrib import admin
from .models import Choice, Question, Image

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,ImageInline]
    
admin.site.register(Question, QuestionAdmin)

# Register your models here.
