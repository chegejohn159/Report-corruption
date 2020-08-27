from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
#from encrypted_model_fields.fields import EncryptedCharField
#from django_cryptography.fields import encrypt
#from fernet_fields import EncryptedCharField
class complain(models.Model):
	name=models.CharField(max_length=128)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
class corruptiontype(models.Model):
	name=models.CharField(max_length=128)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
class entity(models.Model):
	name=models.CharField(max_length=128)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name
class county(models.Model):
	name=models.CharField(max_length=128)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.name


class usermanager(BaseUserManager):		
	def create_user(self,email,password,firstname,lastname,national_id):
		user=self.model(email=email,password=password,firstname=firstname,lastname=lastname,national_id=national_id)
		user.set_password(password)
		user.is_staff=False
		user.is_superuser=False
		user.save(using=self._db)
		return user
	def create_superuser(self,email,password,firstname,lastname,national_id):
		user=self.create_user(email=email,password=password,firstname=firstname,lastname=lastname,national_id=national_id)
		user.is_active=True
		user.is_staff=True
		user.is_superuser=True
		user.save(using=self._db)
		return user
class user(AbstractBaseUser,PermissionsMixin):
	password=models.CharField(max_length=100)
	email=models.EmailField(unique=True)
	firstname=models.CharField(max_length=30)
	lastname=models.CharField(max_length=30)
	national_id=models.IntegerField()
	is_staff=models.BooleanField(default=False)
	is_police=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	is_Eacc=models.BooleanField(default=False)
	REQUIRED_FIELDS=['firstname','lastname','national_id']
	USERNAME_FIELD='email'

	objects=usermanager()

	def __str__(self):
		return self.email
	def get_short_name(self):
		return self.email


class corruption(models.Model):
	complain=models.ForeignKey(complain, on_delete=models.CASCADE)
	corruptiontype = models.ForeignKey(corruptiontype, on_delete=models.CASCADE)
	entity = models.ForeignKey(entity, on_delete=models.CASCADE)
	county=models.ForeignKey(county, on_delete=models.CASCADE)
	description = models.CharField(max_length=128)
	cityortown=models.CharField(max_length=128)
	name=models.CharField(max_length=128,null=True)
	phone=models.CharField(max_length=128,null=True)
	police=models.ForeignKey(user,models.SET_NULL,blank=True, null=True)
	done=models.BooleanField(default=False)
	
	def __str__(self): # For Python 2, use __unicode__ too
		return self.description
class reportchallenges(models.Model):
	corruption= models.ForeignKey(corruption, on_delete=models.CASCADE)
	description = models.CharField(max_length=128)
	police= models.ForeignKey(user, on_delete=models.CASCADE)
	def __str__(self): # For Python 2, use __unicode__ too
		return self.description







