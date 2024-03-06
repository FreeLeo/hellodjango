from django.contrib import admin

# Register your models here.
from study.models import Person, TbDept


class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    search_fields = ('name', )
    ordering = ('name', )


class TbDeptModelAdmin(admin.ModelAdmin):
    list_display = ('dno', 'dname', 'dloc')
    search_fields = ('name', )
    ordering = ('dno', )


admin.site.register(Person, PersonModelAdmin)
admin.site.register(TbDept, TbDeptModelAdmin)