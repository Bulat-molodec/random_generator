from django import forms

class RandomAlphanumericForm(forms.Form):
    number_of_characters = forms.IntegerField(
        label="Введите желаемую длину пароля:",
        min_value=4,
        max_value=50,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
