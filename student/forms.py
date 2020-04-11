from django import forms
import re
from .models import Student,Classes,StudentInClass,MyUser,Area
class CreationForm(forms.ModelForm):
    #name =forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Tên học sinh "}))
    #birtday=forms.DateField(widget=forms.DateInput(attrs={"placeholder":"Ngày sinh"}))
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name',None)
        self.phone_number_1 = kwargs.pop('phonenum1',None)
        self.learning_area = kwargs.get('area',None)
        super().__init__(*args, **kwargs)
    # def clean_phonenumber(self):
    #     if 'Student.phone_number_1' in self.cleaned_data:
    #         if not re.search(r'^\d+$', Student.phone_number_1): # không - tìm thấy - các kí tự số
    #             raise forms.ValidationError("Số điện thoại có kí tự đặc biệt")
    #         return Student.phone_number_1
    # def save(self,commit=True):
    """ Không hiểu sao khi add đoạn này vào thì nó sai nên để thế này luôn """
    #     student = super().save(commit=False)
    #     student.name = self.name
    #     student.phone_number_1 = self.phone_number_1
    #     student.learning_area = self.learning_area
    #     student.save()

    class Meta:
        model = Student
        Student.is_learning=False
        fields = ["name","phone_number_1","learning_area"]
    
class TimeStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInClass
        fields = ["class_id"]