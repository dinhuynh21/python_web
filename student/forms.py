from django import forms
import re
from .models import Student,Class
class CreationForm(forms.ModelForm):
    class Meta:
        model = Student
        Student.status=False
        fields = ["name","birtday","address","phonenum1"]
    def clean_phonenumber(self):
        if 'Student.phonenum1' in self.cleaned_data:
            if not re.search(r'^\w+$', Student.phonenum1):
                raise forms.ValidationError("Số điện thoại có kí tự đặc biệt")
            return Student.phonenum1
class TimeStudentForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ["systemlevel","dayStart","dayEnd"]