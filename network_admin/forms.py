from django import forms


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))



	def __init__(self):
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus'
            'required': 'required', 'placeholder': 'User Name'})
        self.fields['password'].widget.attrs.update({
            'required': 'required', 'placeholder': 'Password'})