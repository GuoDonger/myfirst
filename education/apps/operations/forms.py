import re
from django import forms
from django.forms import fields
from .models import UserAskInfo, UserCommentInfo


# model和form结合
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAskInfo
        fields = '__all__'    # 添加所有
        exclude = ['add_time']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        flag = re.match(r'1[34578]\d{9}', phone)
        if flag:
            return phone
        else:
            raise forms.ValidationError('非有效手机号')


class UserCommentForm(forms.Form):
    content = fields.CharField(max_length=300, min_length=1, required=True)
    course_id = fields.IntegerField(required=True)
