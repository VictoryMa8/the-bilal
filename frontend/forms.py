from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'A descriptive title...'}),
            'description': forms.TextInput(attrs={'class': 'input mt-5', 'placeholder': 'A descriptive description...'}),
        }

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Applying custom attributes to password fields from UserCreationForm
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter a username',
            'class': 'border-2 border-blue-900',
            'label': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter a password...',
            'class': 'border-2 border-blue-900',
            'label': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat your password...',
            'class': 'border-2 border-blue-900',
            'label': 'Repeat Password'
        })