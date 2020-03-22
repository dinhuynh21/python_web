from django.contrib import admin
from .models import Student,Area,Book,SystemLevel,CambridgeLevel,Teacher,Classes,StudentInClass,Fee,MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CreationForm
from django.contrib.auth.models import User

from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
# Register your models here.
class StudentInLine(admin.TabularInline):
    model=StudentInClass # model hỗ trợ
    #fields=['student','class_id']
    def get_extra(self, request, obj=None, **kwargs):# hàm giới hạn lượng obj "trống" ở [inline]
        extra = 1
        # if obj:
        #     return extra - obj.StudentInClass_set.count() # không rõ là cái gì :V
        return extra
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "class_id":  #dòng này có vấn đề
            #Có lỗi nhưng nó vẫn chạy tốt :V méo hiểu kệ nó 
            # Fix 1: Import thêm pylint vào project sau đó vào settings.json(Python) import thêm 1 đoạn code gọi plugin pylint là dc 
            a=MyUser.objects.get(user=request.user) # Lấy MyUser theo user đang có
            # Lọc theo khu vực của User
            kwargs["queryset"] = Classes.objects.filter(area=a.area) # Student.objects.filler() thì k sao vì model có Manage()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# More infomation to User in admin
class MyUserInline(admin.StackedInline):
    model=MyUser
    extra=1
    can_delete=False
    verbose_name = 'Khu vực' # Tên từng phần tử trong inline
    verbose_name_plural = 'Chức năng' # Tên cả phân vùng chức năng, (phần màu xanh của mục)
class UserAdmin(BaseUserAdmin):
    inlines=(MyUserInline,)


class FeeInLine(admin.TabularInline):
    model=Fee
    extra=1  
    fields=['student','class_id','level','course_date','fee','receipt_number']
    verbose_name='Phiếu thu'
    verbose_name_plural = 'Học phí'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "class_id":
            user = MyUser.objects.get(user=request.user)
            kwargs["queryset"]= Classes.objects.filter(area=user.area)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
class StudentAdmin(admin.ModelAdmin): # danh sách học sính
    list_display=['name', 'phone_number_1','joined_date'] # danh sách hiển thị, có thể nhóm các thuộc tính 
    search_fields=['name','phone_number_1'] # Thanh tìm kiếm ['foreign_key__related_fieldname']
    #fields= [('birtdate','address')] # chọn trường hiển thị và gộp nhóm (fail)
    list_filter=[('learning_area', admin.RelatedOnlyFieldListFilter)]# phần màu cam là lọc theo 'tên_thuộc_tính', phần màu trắng thì k rõ :V
    list_per_page = 30
    ordering = ['name'] # sắp xếp
    paginator= 15

    inlines=[StudentInLine,FeeInLine] # Thêm 1 inline obj
    #exclude =['name']  #loại trừ thuộc tính ('name') 
    #save_on_top=True  # đưa thêm các button save lên trên cùng của model
    #raw_id_fields = ["learning_area",] # chuyễn về dạng id của field learning_area (xấu)
    #radio_fields = {"learning_area": admin.VERTICAL}# đổi từ list choose sang chọn A B C theo số lượng có của FK

    # readonly_fields = ('address_report',)
    # def address_report(self, instance):
    #     # assuming get_full_address() returns a list of strings
    #     # for each line of the address and you want to separate each
    #     # line by a linebreak
    #     return format_html_join(
    #         mark_safe('<br>'),
    #         '{}',
    #         ((line,) for line in instance.get_full_address()),
    #     ) or mark_safe("<span class='errors'>I can't determine this address.</span>")
    # address_report.short_description = "Address 1111" # phương thức hiển thị

    def upper_case_name(self,obj): # gọi vào list_display và hiển thị nó như các obj bình thường
        return ("%s %s" %(obj.name,obj.phone_number_1)).upper() # hiện tại không dùng tới
    upper_case_name.short_description='Name'

    

class AreaAdmin(admin.ModelAdmin): # danh sách khu vực
    list_display=['name']
    search_fields=['name']   
class BookAdmin(admin.ModelAdmin):# danh sách Sách
    list_display=['name','fee','note']
    search_fields=['name']
    ordering = ['name']
class SystemLevelAdmin(admin.ModelAdmin):# Danh sách level 
    list_display=['name','fee','note']
    search_fields=['name']
    ordering = ['name']

class TeacherAdmin(admin.ModelAdmin):# danh sách giáo viên
    list_display=['name','email']
    search_fields=['name','phone_number','email']
    list_filter = ['area']
    ordering = ['name']

class ClassAdmin(admin.ModelAdmin): #Danh sách lớp
    list_display=['name','area','start_date','end_date']
    search_fields=['name']
    list_filter=['shift','area']
    inlines=[StudentInLine]

class CambridgeLevelAdmin(admin.ModelAdmin):# Danh sách Level Cambridge
    list_display=['name','fee','note']
    search_fields=['name']

class FeeAdmin(admin.ModelAdmin): # Danh sách thu học phí theo biên lai
    list_display=['student','class_id','receipt_number','fee']
    app_label="học phí"
    search_fields=['receipt_number','student__name','payment_date'] # Gọi API ['(foreign_key)__(related_fieldname)'] thực tế là ['foreign_key__related_fieldname']
    
# Untake User default
admin.site.unregister(User)
# Đưa cái đã tạo lên Admin site
admin.site.register(User, UserAdmin)

# Đưa các class đã tạo lên admin quản lí
admin.site.register(Student, StudentAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(SystemLevel, SystemLevelAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Classes,ClassAdmin)
admin.site.register(CambridgeLevel, CambridgeLevelAdmin)
admin.site.register(Fee,FeeAdmin)

admin.site.site_header = "QUẢN TRỊ AIES"
admin.site.site_title = "Trang quản lí thông tin"
admin.site.index_title="Hệ thống lưu trữ thông tin" #admin.AdminSite cùng chức năng AdminSite.site
#admin.site.register(SystemLevel, SystemLevelAdmin)