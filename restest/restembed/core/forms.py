from django import forms

#class SubmitEmbed(forms.Form):
#    url = forms.URLField()
    
class SubmitEmbed(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length=100)
 
