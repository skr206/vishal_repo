from django.contrib import admin
from testapp1 .models import Student109qwe
# Register your models here.
@admin.register(Student109qwe)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','email','branch']