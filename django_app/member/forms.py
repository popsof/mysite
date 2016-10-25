from django import forms
from .models import MyUser
from django.contrib.auth import password_validation


class SignupModelForm(forms.ModelForm):
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model=MyUser
        fields = ( 'email', 'password1', 'password2', 'last_name', 'first_name', 'nickname', )

        widgets = {
            'email': forms.EmailInput( attrs={'class': 'form-control'} ),
            'last_name': forms.TextInput( attrs={'class': 'form-control'} ),
            'first_name': forms.TextInput( attrs={'class': 'form-control'} ),
            'nickname': forms.TextInput( attrs={'class': 'form-control'} ),
        }


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        password_validation.validate_password(
            self.cleaned_data['password1'], self.instance )



    def save(self, commit=True):
        user = super(SignupModelForm, self).save( commit=False )
        user.set_password( self.clean_data['password1'] )
        user.save()

        return user



# fields = ('email', 'password', 'last_name', 'first_name', 'nickname', 'is_staff')


class SignupForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        error_messages={ 'invalid': '이메일 형식이 아닙니다.' },
        widget=forms.EmailInput( attrs={'class': 'form-control' } )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        max_length=20,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    first_name = forms.CharField(
        max_length=20,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    nickname = forms.CharField(
        max_length=24,
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    # date_joined = forms.DateTimeField()
    # is_staff = forms.BooleanField


    #
    # class Meta:
    #     model = MyUser
    #     fields = ('email', 'password', 'last_name', 'first_name', 'nickname', 'is_staff')
