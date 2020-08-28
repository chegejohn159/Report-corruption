from django import forms
# from fernet_fields import EncryptedCharField
from .models import *

class corruptions(forms.ModelForm):
	complain= forms.ModelChoiceField(queryset=complain.objects.all(),initial='')
	corruptiontype = forms.ModelChoiceField(queryset=corruptiontype.objects.all(),initial='')
	entity = forms.ModelChoiceField(queryset=entity.objects.all(),initial='')
	county=forms.ModelChoiceField(queryset=county.objects.all(),initial='')
	description=forms.CharField(max_length=2000,widget=forms.Textarea())
	cityortown=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'City or Town'}))
	name=forms.CharField(required=False,widget=forms.TextInput(attrs={'size':30,'placeholder':'Full name (Optional)'}))
	phone=forms.CharField(required=False,widget=forms.TextInput(attrs={'size':30,'placeholder':'Phone number (Optional)'}))
	class Meta:
		model = corruption
		fields = ('complain','corruptiontype', 'entity','county','description','cityortown','name','phone')
class reportchallenge(forms.ModelForm):
	corruption = forms.ModelChoiceField(queryset=corruption.objects.all(),initial='')
	description=forms.CharField(max_length=2000,widget=forms.Textarea())
	class Meta:
		model = reportchallenges
		fields = ('corruption', 'description')
class signup(forms.ModelForm):
	firstname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your  First_Name'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your  Last_Name'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':30,'placeholder':'Type your password'}))
	national_id=forms.IntegerField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter your National_id'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Email Address'}))
	class Meta:
		model = user
		fields = ('firstname','national_id','lastname', 'email','password',)  

class eaccsignup(forms.ModelForm):
	firstname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your First_Name'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Last_Name'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':30,'placeholder':'Type your password'}))
	national_id=forms.IntegerField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter your National_id'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Email Address'}))
	class Meta:
		model = user
		fields = ('firstname','national_id','lastname', 'email','password',)  