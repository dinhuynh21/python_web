from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

# Create your models here.
# Qui tắc đặt tên biến : Tên model không có gạch dưới nên viết hoa,
# Tên field thì đặt bằng các dấu gạch chân

class Area(models.Model):
    name= models.CharField(max_length=50)   
    def __str__(self):
        return self.name

class MyUser(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    area=models.ForeignKey(Area,on_delete=models.DO_NOTHING )
    # def __str__(self):
    #     return self.area

class Student(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100) #1
    birtdate = models.DateField(blank=True,null=True,)  #2   # '2019-09-08' or (2018 , M, D) chua thu
    address = models.TextField(max_length=200,null=True,blank=True)  #3
    phone_number_1 = models.CharField(max_length=12)  #4
    phone_number_2 = models.CharField(default='',max_length=12,null=True,blank=True)
    identity_number = models.CharField(max_length=10,default='',null=True,blank=True)
    learning_area = models.ForeignKey(Area,on_delete=models.DO_NOTHING,related_name='learning_area')
    is_learning = models.BooleanField(default=True)  #True = đang học, False=Khác
    joined_date = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=200,null=True,blank=True)

    #def get_student_not_paid_fee(self):
    #def decade_born_in(self):
        #import datetime
        #return self.birtdate.strftime('%Y')[:3] + "0's"
    #decade_born_in.short_description = 'Birth decade'
    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(max_length=100)
    fee=models.IntegerField(default=0)
    note=models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

class SystemLevel(models.Model):
    name=models.CharField(max_length=100)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='books')
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    fee = models.IntegerField(default=0)
    note = models.TextField(max_length=200,default='',blank=True)

    def __str__(self):
        return self.name

class CambridgeLevel(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField(default=0)
    note = models.TextField(max_length=200,default='',blank=True)
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    is_male = models.BooleanField(default=False) # False = nữ , True =nam
    area = models.ForeignKey(Area,on_delete=models.DO_NOTHING,related_name='area')
    birthdate = models.DateField(null=False)
    address= models.TextField(max_length=100,default='',blank=True)
    phone_number = models.CharField(default='',max_length=12)
    email = models.EmailField()
    identity_number = models.CharField(max_length=10,default='')
    note = models.TextField(max_length=100,default='',blank=True)
    
    def save(self, *args, **kwargs):
        #from django.contrib.auth.models import User
        if (self.is_male == True):
            if ('Mr.' not in self.name):
                self.name = "Mr. %s" %(self.name.title()) # fail ở đây (title là viết hoa chữ đầu mỗi từ)
            #super().save(*args, **kwargs)
        else :
            if ('Ms.'not in self.name):
                self.name = "Ms. "+self.name.title() # fail ở đây nữa :V
        #self.note = User.objects.get(settings.AUTH_USER_MODEL).name
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=100, blank=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teachers')
    area = models.ForeignKey(Area,on_delete=models.CASCADE,related_name='areas')
    level = models.ForeignKey(SystemLevel,on_delete=models.CASCADE,related_name='levels')
    members = models.ManyToManyField(Student, through='StudentInClass') # Xài models Student nhưng truyền vào/ra ? là StudentInClass
    #numberOfStudent=models.IntegerField(default=0) # khong nen xai bien nay ???
    room = models.CharField(max_length=20)
    shift = models.CharField(max_length=20,default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(max_length=200,default='',blank=True)
    def __str__(self):
        return '%s %s'%(self.area,self.name)
        #return "%s %s" % (self.shift, self.start_date)
    # def _level_name(self):
    #     return self.level
    # def course_date(self):
    #     return "%s %s" % (self.start_date,self.end_date)
    # course_date.short_description='Course date' # phương thức hiển thị cho def này  
    def save(self, *args, **kwargs):
        self.name = self.level.name + " " + self.teacher.name + " ca " + format(self.shift)
        #self.name = self.level.name
        super().save(*args, **kwargs)

class Fee(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes,on_delete=models.CASCADE,related_name='classer')
    level = models.CharField(max_length=50,blank=True) 
    course_date = models.CharField(max_length=50,blank=True)
    fee = models.IntegerField(default=0)
    receipt_number = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True,) # Hơi sai sai vs thực tế :V
    note = models.TextField(max_length=100,default='',blank=True)

    def __str__(self):
        return "%s %s %s" %(self.receipt_number,self.student.name,self.level)
    
    # def __init__(self):
    #     get_class=StudentInClass.objects.get(student=self.student)
    #     class_id = Classes.objects.filter(get_class)
    #     super().__init__(self)
    
    def save(self, *args, **kwargs):
        #if self.level == None:
            self.level = self.class_id.name
            self.course_date = "%s -- %s" % (Classes.__getattribute__(self.class_id,'start_date') , Classes.__getattribute__(self.class_id,'end_date'))
            self.note = "Ngày lập phiếu: %s" % (self.payment_date)
            super().save(*args, **kwargs)
        #else:
            #super().save(*args, **kwargs)
class StudentInClass(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    
    # def filter(self):
    #     self.class_id = filter(Student.__getattribute__(self.student,'learning_area'))
    #     return self.class_id

# class Gift(models.Model):
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     number=models.IntegerField(default=0)
#     releas_day=models.DateField(auto_now_add=True)
#     note=models.TextField(max_length=100,default='',blank=True)
#     def __str__(self):
#         return self.student

# class BorrowPayBook(models.Model):
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
#     book=models.ForeignKey(Book,on_delete=models.CASCADE)
#     number=models.IntegerField(default=1)
#     release_day=models.DateField(auto_now_add=True)
#     status=models.BooleanField(default=True) # True = Vẫn còn nợ, False = Đã trả nợ
#     note=models.TextField(max_length=100,default='',blank=True)
#     def __str__(self):
#         return self.student

# class ExamCambridge(models.Model):
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
#     cambridge_level=models.ForeignKey(CambridgeLevel,on_delete=models.CASCADE)
#     exam_day=models.DateField()
#     waiting_result=models.BooleanField(default=True)
#     passed=models.BooleanField(default=False)
#     note=models.TextField(max_length=100,default='',blank=True)
#     def __str__(self):
#         return self.student
    
# class StudentWaitClass(models.Model):
#     student=models.ForeignKey(Student,on_delete=models.CASCADE)
#     system_level=models.ForeignKey(SystemLevel,on_delete=models.CASCADE)
#     note=models.TextField(max_length=100,default='',blank=True)
#     def __str__(self):
#         return self.student




# class Position(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     position=models.CharField(max_length=50)
