from django.contrib import admin
from .models import Student,Area,Book,SystemLevel,CambridgeLevel,Teacher,Class,StudentInClass
# Register your models here.
class StudentInLine(admin.TabularInline):
    model=StudentInClass

class StudentAdmin(admin.ModelAdmin):
    list_display=['name', 'phonenum1']
    search_fields=['name']
    
    inlines=[StudentInLine]

class AreaAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']   
class BookAdmin(admin.ModelAdmin):
    list_display=['name','fee','note']
    search_fields=['name']
class SystemLevelAdmin(admin.ModelAdmin):
    list_display=['name','fee','note']
    search_fields=['name']
class TeacherAdmin(admin.ModelAdmin):
    list_display=['name','gender','email']
    search_fields=['name']
class ClassAdmin(admin.ModelAdmin):
    list_display=['name','area','dayStart','dayEnd']
    search_fields=['name']
    list_filter=['shift','area']
    inlines=[StudentInLine]

class CambridgeLevelAdmin(admin.ModelAdmin):
    list_display=['name','fee','note']
    search_fields=['name']
admin.site.register(Student, StudentAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(SystemLevel, SystemLevelAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(CambridgeLevel, CambridgeLevelAdmin)
#admin.site.register(SystemLevel, SystemLevelAdmin)