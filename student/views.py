from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from student.models import Student,Class,StudentInClass
from .forms import CreationForm,TimeStudentForm
from django.views.generic import ListView, DetailView
# Create your views here.
class StudentListView(ListView): 
    queryset = Student.objects.all()
    template_name = 'student/student.html'
    context_object_name = 'Students' # đặt tên truyền vào Temp
    paginate_by = 10  #phân trang
#class StudentDetailView(DetailView): # Trang info student
   # model = Student
   # template_name = 'student/detailStudent.html'
def DetailStudent(request,pk):
    student = get_object_or_404(Student,pk=pk) # chỉ định tham số pk 
    
    #form = TimeStudentForm()
    return render(request, 'student/detailStudent.html', {'student':student,} )

def CreateStudent(request):
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/student")
        return HttpResponse("Dữ liệu không hợp lệ")
    return render(request, 'student/createStudent.html', {'form':form})

def test(request):
    return render(request,'pages/base2.html')
