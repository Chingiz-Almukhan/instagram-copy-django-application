from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


GENDER = (('male', 'Мужской'), ('female', 'Женский'), ('other', 'Другое'))


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(min_length=5, max_length=50,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.CharField(min_length=7, max_length=70, required=True,
                            widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    avatar = forms.ImageField(required=True)
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    gender = forms.ChoiceField(label='Пол', choices=GENDER, widget=forms.RadioSelect())

    class Meta:
        model = get_user_model()
        fields = (
            'username', 'email', 'avatar', 'password', 'password_confirm', 'first_name', 'biography', 'phone_number',
            'gender')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Пароли не совпадают')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    gender = forms.ChoiceField(label='Пол', choices=GENDER, widget=forms.RadioSelect)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'biography', 'phone_number', 'email', 'avatar', 'gender')
