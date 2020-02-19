from django import forms
import re
from .models import Student,Class,StudentInClass
class CreationForm(forms.ModelForm):
    #name =forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Tên học sinh "}))
    #birtday=forms.DateField(widget=forms.DateInput(attrs={"placeholder":"Ngày sinh"}))
    class Meta:
        model = Student
        Student.is_learning=False
        fields = ["name","birtdate","address","phone_number_1"]
    def clean_phonenumber(self):
        if 'Student.phonenum1' in self.cleaned_data:
            if not re.search(r'^\w+$', Student.phone_number_1):
                raise forms.ValidationError("Số điện thoại có kí tự đặc biệt")
            return Student.phone_number_1
class TimeStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInClass
        fields = ["class_id"]