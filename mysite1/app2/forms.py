from django import forms


from app2.models import SettingModel
from django import forms


# creating a form
CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]
class SettingsForm(forms.ModelForm):
    receive_newsletter = forms.CharField(widget=forms.CheckboxInput,required=False)
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
    sex = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    dob = forms.DateField(label='DOB', widget=forms.DateInput)
    class Meta:
        model = SettingModel
        fields = ['receive_newsletter','days','sex','dob']
