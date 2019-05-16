from django import forms
from .models import Rating
from django.conf import settings # user를 사용하기 위해서?

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['comment', 'score', 'movie', 'user']
        
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder':'영화 감상평을 입력하세요.', 'class':'comment'}),
            'score': forms.IntegerInput(attrs={'placeholder':'영화 평점을 입력하세요.', 'class':'score'}),
        }
        
        error_messages = {
            'comment': {'required':'영화 감상평을 입력하세요.'},
            'score': {'required':'영화 평점을 입력하세요.'},
        }