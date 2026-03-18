from django.contrib.auth.forms import UserCreationForm

# Django doesn't want to assume how we want our sign up form to be
# Thus, we have to declare it manually
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Applying custom attributes to password fields from UserCreationForm
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter a username',
            'label': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter a password...',
            'label': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Repeat password...',
            'label': 'Password'
        })