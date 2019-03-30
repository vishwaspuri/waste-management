from django import forms
from .models import People,Worker,Bin

class CleanGarbageForm(forms.ModelForm):#filled by people
	class Meta:
		model=Bin
		fields = ('green_waste','blue_waste')

class PeopleForm(forms.ModelForm):
	class Meta:
		model = People
		fields = ('name','pic','city')

class WorkerForm(forms.ModelForm):
	class Meta:
		model = Worker
		fields = ('name','pic','city')
