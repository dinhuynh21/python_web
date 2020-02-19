from django.contrib import admin
from .models import Student,Area,Book,SystemLevel,CambridgeLevel,Teacher,Class,StudentInClass,Fee
from .forms import CreationForm
# Register your models here.
class StudentInLine(admin.TabularInline):
    model=StudentInClass

    

class StudentAdmin(admin.ModelAdmin):
    list_display=['name', 'phone_number_1','joined_date']
    search_fields=['name','phone_number_1']
    list_filter=['learning_area',]
    ordering = ['name']
    inlines=[StudentInLine]

    def upper_case_name(self,obj): #gọi vào list_display và hiển thị nó như các obj bình thường
        return ("%s %s" %(obj.name,obj.phone_number_1)).upper() # hiện tại không dùng tới
    upper_case_name.short_description='Name'

    

class AreaAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']   
class BookAdmin(admin.ModelAdmin):
    list_display=['name','fee','note']
    search_fields=['name']
    ordering = ['name']
class SystemLevelAdmin(admin.ModelAdmin):
    list_display=['name','fee','note']
    search_fields=['name']
    ordering = ['name']

class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','email']
    search_fields=['name','phone_number','email']
    ordering = ['name']

class ClassAdmin(admin.ModelAdmin):
    list_display=['name','area','start_date','end_date']
    search_fields=['name']
    list_filter=['shift','area']
    inlines=[StudentInLine]

class CambridgeLevelAdmin(admin.ModelAdmin):
    list_display=['name','fee','note']
    search_fields=['name']

class FeeAdmin(admin.ModelAdmin):
    list_display=['student','class_id','receipt_number','fee']
    search_fields=['name']
    

admin.site.register(Student, StudentAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(SystemLevel, SystemLevelAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(CambridgeLevel, CambridgeLevelAdmin)
admin.site.register(Fee,FeeAdmin)

admin.site.site_header = "QUẢN TRỊ AIES"
admin.site.site_title = "Trang quản lí thông tin"
#admin.site.register(SystemLevel, SystemLevelAdmin)