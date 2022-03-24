from django import forms
from cruidapp.models import Students
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
