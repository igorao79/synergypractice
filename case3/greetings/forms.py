from django import forms


class NameForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Ваше имя',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите ваше имя',
            'class': 'form-input',
            'autocomplete': 'off',
        }),
        error_messages={
            'required': 'Пожалуйста, введите ваше имя.',
        },
    )

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Имя не может состоять только из пробелов.')
        if len(name) < 2:
            raise forms.ValidationError('Имя должно содержать минимум 2 символа.')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Имя не должно содержать цифры.')
        return name
