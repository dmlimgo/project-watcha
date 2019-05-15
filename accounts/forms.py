from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile
class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserCustomCreationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
        #     field.label=''
            field.help_text=''
        self.fields['username'].label='아이디'
        self.fields['email'].label='이메일'
        self.fields['password1'].label='비밀번호'
        self.fields['password2'].label='비밀번호 확인'
        self.fields['username'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})
        self.fields['email'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})
        self.fields['password1'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})
        self.fields['password2'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})
        
class AuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password',)
        
    def __init__(self, *args, **kwargs):
        # self.css_class = 'test'
        kwargs.setdefault('label_suffix', '')
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        # for key, field in self.fields.items():
        #     field.label=key
        self.fields['username'].label='아이디'
        # self.fields['username'].label.__class__='test'
        print(dir(self.fields['username']))
        
        self.fields['username'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})
        self.fields['password'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label=''
        self.fields['nickname'].widget.attrs.update({'placeholder': '사용자 이름', 'class': 'input-box'})
        self.fields['introduction'].widget.attrs.update({'placeholder': '소개', 'class': 'input-box'})