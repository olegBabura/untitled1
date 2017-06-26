from django import forms


class InputForm(forms.Form):
    u_city = forms.CharField(label=(), max_length=30,)
