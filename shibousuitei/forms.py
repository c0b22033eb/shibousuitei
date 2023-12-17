from django import forms

class AgeForm(forms.Form):
    age = forms.IntegerField(label='現在の年齢', min_value=0, max_value=120)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['class'] = 'form-control col-3'
        # self.fields['age'].widget.attrs['placeholder'] = '年齢をここに入力してください。'