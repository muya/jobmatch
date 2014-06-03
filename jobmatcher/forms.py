from django.forms import ModelForm
from jobmatcher.models import Job

class PostJobForm(ModelForm):
	class Meta:
		model = Job
		fields = ['name', 'description', 'valid_until', 'job_owner']
			