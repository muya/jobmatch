from django.contrib import admin
from jobmatcher.models import JobOwner
from jobmatcher.models import JobSeeker
from jobmatcher.models import Job

class JobOwnerAdmin(admin.ModelAdmin):
	fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'status']

class JobSeekerAdmin(admin.ModelAdmin):
	fields = ['first_name', 'last_name', 'email_address', 'phone_number', 'status']

class JobsAdmin(admin.ModelAdmin):
	fields = ['name', 'description', 'valid_until', 'job_owner', 'status']
		

admin.site.register(JobOwner, JobOwnerAdmin)
admin.site.register(JobSeeker, JobSeekerAdmin)
admin.site.register(Job, JobsAdmin)
# Register your models here.
