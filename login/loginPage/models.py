from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

import datetime


# Create your models here.

@python_2_unicode_compatible
class UserDetail(models.Model):
	login_id = models.CharField(max_length=256)
	login_challenge = models.CharField(max_length=256)
	created = models.DateTimeField('date published')

	def __str__(self):
		return self.login_id
'''
	def is_created_5days_ago(self):
		return self.created >= timezone.now() - datetime.timedelta(days=5)

	def getLoginId(self):
		return self.login_id

	def getLoginChallenge(self):
		return self.login_challenge
'''