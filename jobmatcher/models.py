from django.db import models
from datetime import datetime
from time import strftime


#
# Custom field types in here.
#
class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ=['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        return datetime.from_timestamp(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value==None:
            return None
        return strftime('%Y%m%d%H%M%S',value.timetuple())

    def to_python(self, value):
        return value

# Create your models here.
class JobOwner(models.Model):
	"""describes a user who can post jobs (employer)"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.EmailField(max_length=255, unique=True)
	phone_number = models.CharField(max_length=20, unique=True)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_modified = UnixTimestampField(auto_created=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name


class JobSeeker(models.Model):
	"""describes a user who can apply for jobs (potential employee)"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email_address = models.EmailField(max_length=255, unique=True)
	phone_number = models.CharField(max_length=20, unique=True)
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_modified = UnixTimestampField(auto_created=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Job(models.Model):
	"""describes a job"""
	name = models.CharField(max_length=100)
	description = models.TextField()
	job_owner = models.ForeignKey(JobOwner)
	valid_until = models.DateTimeField("date until which the job is available")
	date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
	date_modified = UnixTimestampField(auto_created=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

		
		