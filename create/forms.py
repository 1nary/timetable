from django import forms
from create.models import Lecture

class createForm(forms.ModelForm):
  class Meta:
    model = Lecture
    fields = ['name','teacher','room','week','period']
    widgets = {
      'name': forms.TextInput(attrs= {
        'placeholder': '講義を入力してください',
        'class': 'form__input form__input-type--text',
      }),
      'teacher':forms.TextInput(attrs= {
        'placeholder': '担当教員を入力してください',
        'class': 'form__input form__input-type--text',
      }),
      'room': forms.TextInput(attrs= {
        'placeholder': '教室を入力してください',
        'class': 'form__input form__input-type--text',
      }),
      'week': forms.RadioSelect(attrs={'class': 'form__input form__input-type--radio'}),
      'period': forms.RadioSelect(attrs={'class': 'form__input form__input-type--radio'})
    }

    
# class createForm(forms.Form):
#   data_week = [
#       ('1','月曜'),
#       ('2','火曜'),
#       ('3','水曜'),
#       ('4','木曜'),
#       ('5','金曜'),
#       ('6','土曜'),
#   ]
#   select_week = forms.ChoiceField(
#     choices=data_week,
#     # initial=1,
#     label='曜日',
#     widget = forms.widgets.RadioSelect(
#       attrs={
#         'class':"form__input form__input-type--radio"
#       }
#     )
#   )

#   data_period = [
#       ('1','１限'),
#       ('2','２限'),
#       ('3','３限'),
#       ('4','４限'),
#       ('5','５限'),
#       ('6','６限'),
#       ('7','７限'),
#   ]
#   select_period = forms.ChoiceField(
#     choices=data_period,
#     # initial=1,
#     label='時限',
#     widget = forms.widgets.RadioSelect(
#       attrs={
#         'class':"form__input form__input-type--radio",
#       }
#     )
#   )

#   name = forms.CharField(
#     required=True,
#     max_length=50,
#     widget=forms.TextInput(
#       attrs= {
#         'placeholder': '講義を入力してください',
#         'class': 'form__input form__input-type--text',
#       }
#     )
#   )
  
#   teacher = forms.CharField(
#     required=False,
#     max_length=50,
#     widget=forms.TextInput(
#       attrs= {
#         'placeholder': '担当教員を入力してください',
#         'class': 'form__input form__input-type--text'
#       }
#     )
#   )

#   room = forms.CharField(
#     required=False,
#     max_length=20,
#     widget=forms.TextInput(
#       attrs= {
#         'placeholder': '教室を入力してください',
#         'class': 'form__input form__input-type--text'
#       }
#     )
#   )
