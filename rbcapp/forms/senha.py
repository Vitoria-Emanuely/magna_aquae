# coding:utf-8

from django import forms

from rbcapp.models import Usuario


class SenhaForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True'}
        )
    )

    password_check = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': 'True'}
        )
    )

    class Meta:
        model = Usuario
        exclude = ('date_joined', 'is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser', 'is_active', 'first_name', 'last_name', 'email', 'username')

    def save(self, commit=True):
        user = super(SenhaForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()