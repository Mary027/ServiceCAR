from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Car, Order

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label=('Имя пользователя'),
        help_text=('Обязательное. 150 символов или меньше. Буквы, цифры и @/./+/-/_ только.'),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    email = forms.EmailField(
        label=('Адрес электронной почты'),
        help_text=('Введите действительный адрес электронной почты.'),
        required=True,
        widget=forms.EmailInput()
    )
    password1 = forms.CharField(
        label=('Пароль'),
        help_text=(' Ваш пароль должен содержать не менее 8 символов.'
                    ' Ваш пароль не может состоять только из цифр.'),
        required=True,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=('Подтверждение пароля'),
        help_text=('Введите тот же пароль, что и раньше, для подтверждения.'),
        required=True,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=('Имя пользователя'),
        max_length=150,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label=('Пароль'),
        strip=False,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'password']  

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['client', 'model', 'series', 'year']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'service_date', 'description', 'cost']
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date'}),
        }