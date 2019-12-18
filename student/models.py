from django.db import models
from django.conf import settings

# Create your models here.
class Student(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100) #1
    birtday = models.DateField(blank=True,null=True)  #2   # '2019-09-08' or (2018 , M, D) chua thu
    address = models.TextField(max_length=200,null=True,blank=True)  #3
    phonenum1 = models.CharField(max_length=12)  #4
    phonenum2 = models.CharField(default='',max_length=12,null=True,blank=True)
    identityCard = models.CharField(max_length=10,default='',null=True,blank=True)
    status = models.BooleanField(default=True)  #True = đang học, False=Khác
    note = models.TextField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class Area(models.Model):
    name= models.CharField(max_length=50)

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
    name=models.CharField(max_length=100)
    gender = models.BooleanField(default=False) # False = nữ , True =nam
    birthday = models.DateField(null=False)
    address= models.TextField(max_length=100,default='',blank=True)
    phonenum = models.CharField(default='',max_length=12)
    email = models.EmailField()
    identityCard = models.CharField(max_length=10,default='')
    note = models.TextField(max_length=100,default='',blank=True)
    def __str__(self):
        return self.name

class Class(models.Model):
    name=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teachers')
    area=models.ForeignKey(Area,on_delete=models.CASCADE,related_name='areas')
    systemlevel=models.ForeignKey(SystemLevel,on_delete=models.CASCADE,related_name='systemlevels')
    #numberOfStudent=models.IntegerField(default=0) # khong nen xai bien nay ???
    room=models.CharField(max_length=20)
    shift=models.CharField(max_length=20,default=1)
    dayStart=models.DateField()
    dayEnd=models.DateField()
    note=models.TextField(max_length=200,default='',blank=True)
    def __str__(self):
        return self.name

class StudentInClass(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    classid=models.ForeignKey(Class,on_delete=models.CASCADE)
    def __str__(self):
        return self.student.name

class Gift(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    number=models.IntegerField(default=0)
    releaseDay=models.DateField(auto_now_add=True)
    note=models.TextField(max_length=100,default='',blank=True)
    def __str__(self):
        return self.student

class BorrowPayBook(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    number=models.IntegerField(default=1)
    releaseDay=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=True) # True = Vẫn còn nợ, False = Đã trả nợ
    note=models.TextField(max_length=100,default='',blank=True)
    def __str__(self):
        return self.student

class ExamCambridge(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    cambridgeLevel=models.ForeignKey(CambridgeLevel,on_delete=models.CASCADE)
    examday=models.DateField()
    waitResult=models.BooleanField(default=True)
    passed=models.BooleanField(default=False)
    note=models.TextField(max_length=100,default='',blank=True)
    def __str__(self):
        return self.student
    
class StudentWaitClass(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    systemLevel=models.ForeignKey(SystemLevel,on_delete=models.CASCADE)
    note=models.TextField(max_length=100,default='',blank=True)
    def __str__(self):
        return self.student
class Fee(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    classid = models.ForeignKey(Class,on_delete=models.CASCADE)
    fee=models.IntegerField(default=0)
    receipt = models.IntegerField()
    paymentday = models.DateField(auto_now_add=True,)
    note=models.TextField(max_length=100,default='',blank=True)
    def __str__(self):
        return self.classid
class Position(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    position=models.CharField(max_length=50)




