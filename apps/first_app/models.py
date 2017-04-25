from __future__ import unicode_literals
from django.db import models

# Create your models here.



class UserManager(models.Manager):
	def validateUser(self, postData):
		validation_errors =[]
		print postData

	##	if not len(postData['name']):
	##		validation_errors.append("Name is Required")

	##	if not len(postData['username']):
	##		validation_errors.append("Username is Required")

	##	if not len(postData['password']):
	##		validation_errors.append("Password is Required")

	##	if not len(postData['confirmpassword']):
	##		validation_errors.append("Password is Not the Same")

	#	response_to_views = {}
	#	if validation_errors:
		#failed validations 
	#		response_to_views["status"] = False
	#		response_to_views["errors"] = validation_errors
	#	else:
		#passed validations/ create the user
	
		
	#	return response_to_views


class User(models.Model):
	name = models.CharField(max_length = 45)
	username = models.CharField(max_length = 45)
	password = models.CharField(max_length = 45)
	passwordconfirm = models.CharField(max_length = 45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
 
 	objects = UserManager()