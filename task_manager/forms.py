from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(forms.ModelForm):
    # Прописываем поля для нашей регистрации
    first_name = forms.CharField(max_length=150,
                                 label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Имя',
                                                               }))
    last_name = forms.CharField(max_length=150,
                                label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Фамилия',
                                                              }))
    username = forms.CharField(max_length=150,
                               label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Имя пользователя',
                                                             'title': 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.'
                                                             }))
    password1 = forms.CharField(min_length=3,
                                label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Пароль',
                                                                  }))
    password2 = forms.CharField(min_length=3,
                                label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Подтверждение пароля',
                                                                  }))
    class Meta:
        # Для сохранения в таблицу USER используем модель User
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
