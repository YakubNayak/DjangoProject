from django import forms
from myapp4.models import Student
class EmpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"