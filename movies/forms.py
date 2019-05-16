from django import forms
from .models import Rating
from django.conf import settings # user를 사용하기 위해서?

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['movie', 'user']
        
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RatingForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.help_text=''
        self.fields['comment'].label='감상평'
        self.fields['score'].label='평점'
        self.fields['comment'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})
        self.fields['score'].widget.attrs.update({'placeholder': '', 'class': 'input-box'})