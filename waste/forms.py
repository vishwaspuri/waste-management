from django import forms
from .models import People,Worker,Bin

class CleanGarbageForm(forms.ModelForm):#filled by people
	class meta():
		model=Bin
		fields = ('green_waste','blue_waste')

		widgets = {
            'Citizen':forms.TextInput(attrs={'class':'textinputclass'})
        }

		


