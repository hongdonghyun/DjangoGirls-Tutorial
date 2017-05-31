from django import forms


class PostCreateForm(forms.Form):
    title = forms.CharField(
        label='제목',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ㅌ타일트아다으다',
                'class': 'form-control'
            }
        )
    )
    text = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        ),
        required=True
    )
