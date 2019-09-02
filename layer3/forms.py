from django import forms
from .models import Rule


class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = '__all__'
