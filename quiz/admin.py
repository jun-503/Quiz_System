from django.contrib import admin
from .models import Question,Choice,UserAnswer

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of choice fields to display when adding/editing a question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

