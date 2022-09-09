from django import forms


CHOICES = [('webpage', 'Webpage'), ('website', 'Website')]

class CloneForm(forms.Form):
    option = forms.CharField(widget=forms.Select(choices=CHOICES))
    url = forms.CharField(max_length=250)
    project_name = forms.CharField(max_length=100)