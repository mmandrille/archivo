from django import forms

class BuscarForm(forms.Form):
    texto = forms.CharField(max_length=50, help_text='', label='', widget=forms.TextInput(attrs={'placeholder': 'Decreto, Expediente, Resumen, Organismo'}))