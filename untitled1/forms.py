from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        label = 'username',
        max_length=32,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
    )
    password = forms.CharField(
        required = True,
        label = 'Enter password',
        max_length = 32,
        widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    )
    Repassword = forms.CharField(
        required= True,
        label = "Re Enter Password",
        max_length = 32,
        widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter Password'})
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='username',
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        required=True,
        label='Enter password',
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )