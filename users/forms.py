from django import forms

from users.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают !!!')
        return cd['password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ('email', 'first_name', 'last_name', 'phone')    # Один из вариантов записи
        exclude = ('is_active', )                                   # Другой вариант записи