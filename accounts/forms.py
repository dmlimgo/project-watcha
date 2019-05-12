from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserCustomCreationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label=''
            field.help_text=''
        self.fields['email'].widget.attrs.update({'placeholder': '이메일 주소', 'class': 'input-box'})
        self.fields['username'].widget.attrs.update({'placeholder': '사용자 이름', 'class': 'input-box'})
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호', 'class': 'input-box'})
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호 확인', 'class': 'input-box'})
        
class AuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password',)
        
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label=''
        self.fields['username'].widget.attrs.update({'placeholder': '사용자 이름', 'class': 'input-box'})
        self.fields['password'].widget.attrs.update({'placeholder': '비밀번호', 'class': 'input-box'})
    