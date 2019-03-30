from django import forms
from .models import People,Worker,Bin

class CleanGarbageForm(forms.ModelForm):#filled by people
	class Meta:
		model=Bin
		fields = ('green_waste','blue_waste')

		


