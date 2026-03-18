from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class StyledSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Applying custom attributes to password fields from AuthenticationForm
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter a username',
            'id': 'demo-card-form-username',
            'label': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter a password...',
            'id': 'demo-card-form-password"',
            'label': 'Password'
        })

class StyledLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Applying custom attributes to password fields from AuthenticationForm
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter a username',
            'id': 'demo-card-form-username',
            'label': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter a password...',
            'id': 'demo-card-form-password"',
            'label': 'Password'
        })