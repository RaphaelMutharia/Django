from django import forms
from registration.models import Student, Course



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'instructor']
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter course title'}),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': 'Enter course description'}),
            'instructor': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Enter course instructor'})
        }