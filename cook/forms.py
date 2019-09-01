from django.forms import ModelForm
from django import forms
from cook.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'img', 'password']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'img': _('img url'),
            'password': _('password'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
            'img': _('img url을 입력해주세요.'),
            'password': _('password를 입력해주세요'),
        }
        widgets = {
            'password': forms.PasswordInput()
        }
        error_messages = {
            'name': {
                'max_length': _('이름이 너무 깁니다. 30자 이하로 해주세요.'),
            },
            'img': {
                'max_length': _('hi'),
            },
            'password': {
                'max_length': _('hi'),
            },
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)
        }


class UpdateRestaurantForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']
