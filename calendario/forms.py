from django import forms

evento_importante = [
    ('leve', 'Leve'),
    ('importante', 'Importante'),
    ('urgente', 'Urgente'),
]

class FechayHora(forms.TimeInput):
    input_type='datetime-local'
    attrs= {'class':'form-control', 'name':'hora_fecha'}

class SimpleForm(forms.Form):
    nombre = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-control', 'name':'nombre'})
    )
    nota = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 'name':'nota'}),
        label="Nota:"
    )
    hora_fecha = forms.TimeField(
        widget=FechayHora,
        label="Fecha - Hora AM/PM",
    )
    relevancia = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect(attrs= {'name':'relevancia'}),
        choices=evento_importante,
    )

