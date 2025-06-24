from django import forms
from django.contrib.auth.models import User
from apps.usuarios.models import ClienteProfile, LeiloeiroProfile


class ClienteRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Nome de Usuário', max_length=150, help_text='Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True) 

    class Meta:
        model = ClienteProfile
        fields = ['name', 'second_name', 'cell'] 

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está registrado em outra conta.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', 'As senhas não coincidem.')
        return cleaned_data


class LeiloeiroRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Nome de Usuário', max_length=150, help_text='Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = LeiloeiroProfile
        fields = ['name', 'cell'] 

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está registrado em outra conta.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            self.add_error('password2', 'As senhas não coincidem.')
        return cleaned_data