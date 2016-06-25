from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	fields = ('name','availability','location','time','reason')
admin.site.register(posts, ProfileAdmin)

class AbsentAdmin(admin.ModelAdmin):
	fields = ('name','absent','time_start','time_end')
admin.site.register(absent, AbsentAdmin)

class MemberAdmin(admin.ModelAdmin):
	fields = ('name','absent')
admin.site.register(member, MemberAdmin)
