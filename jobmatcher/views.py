from django.shortcuts import render

from jobmatcher.models import Job
from jobmatcher.forms import PostJobForm

# Create your views here.
def post_job(request):
	"""
	function to handle creating new jobs
	"""
	if request.method == 'POST':
		form = PostJobForm(request.POST)
		if form.is_valid():

			return HttpResponseRedirect('/thanks/')
	else:
		form = PostJobForm()

	return render(request, 'jobs/create.html', {'form': form})