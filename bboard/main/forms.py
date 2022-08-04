from django import forms
from django.contrib.auth import password_validation, authenticate, login
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from .models import AdvUser, SuperRubric, SubRubric, Bb, AdditionalImage


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,label='Адрес электронной почты')


    class Meta:
        model = AdvUser
        fields = ('username','email','first_name','last_name','send_messages')


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput,
                                help_text='Введите такой же пароль для проверки')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data['password1']
        password2 = cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError (
                'Введенные пароли не совпадают',code='password_mismatch'
            )}
            raise ValidationError(errors)



    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1','password2','first_name', 'last_name', 'send_messages')


class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(queryset=SuperRubric.objects.all(),empty_label=None,label='Надрубрика',required=True)

    class Meta:
        model = SubRubric
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False,max_length=20,label='')


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {'author':forms.HiddenInput}


AIFormSet = inlineformset_factory(Bb,AdditionalImage,fields='__all__')