import re

from django import forms
from django.core.exceptions import ValidationError


PHONE_PATTERN = r"^((\+?)(?:\d[^A-Z,a-z,@]{10,14}))$"
EMAIL_PATTERN = r"([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]{2,})"


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "ФИО контактного лица",
                "class": "form-control",
                "id": "fullNameLegal",
            }
        ),
    )
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Номер телефона",
                "class": "form-control",
                "id": "validationPhoneNumber",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@example.ru",
                "class": "form-control",
                "id": "email",
            }
        ),
    )

    company_name = forms.CharField(
        label="Наименование организации",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "companyName",
                "placeholder": "Наименование организации",
            }
        ),
    )

    inn = forms.CharField(
        label="ИНН",
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inn",
                "placeholder": "ИНН",
            }
        ),
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"id": "message", "class": "form-control"}),
    )

    company_details = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "multiple": False,
                "allow_empty_file": True,
                "id": "company_details_input",
                "form": "cart_modal_form",
                "class": "form-control",
                "type": "file",
            }
        ),
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        correct_phone_number = PHONE_PATTERN
        if not re.match(correct_phone_number, phone_number.strip()):
            raise ValidationError("Проверьте правильно ли введен номер")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        correct_email = EMAIL_PATTERN
        if not re.match(correct_email, email):
            raise ValidationError(
                "Проверьте правильно ли указана почта для обратной связи"
            )
        return email


class PhysicalContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "ФИО контактного лица",
                "class": "form-control",
                "id": "fullNameLegal",
            }
        ),
    )
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Номер телефона",
                "class": "form-control",
                "id": "validationPhoneNumber",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@example.ru",
                "class": "form-control",
                "id": "email",
            }
        ),
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"id": "message", "class": "form-control"}),
    )

    company_details = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "multiple": False,
                "allow_empty_file": True,
                "id": "company_details_input",
                "form": "cart_modal_form",
                "class": "form-control",
                "type": "file",
            }
        ),
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        correct_phone_number = PHONE_PATTERN
        if not re.match(correct_phone_number, phone_number.strip()):
            raise ValidationError("Проверьте правильно ли введен номер")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        correct_email = EMAIL_PATTERN
        if not re.match(correct_email, email):
            raise ValidationError(
                "Проверьте правильно ли указана почта для обратной связи"
            )
        return email

class MailForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "ФИО контактного лица",
                "class": "form-control",
                "id": "fullNameLegal",
            }
        ),
    )
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Номер телефона",
                "class": "form-control",
                "id": "validationPhoneNumber",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@example.ru",
                "class": "form-control",
                "id": "email",
            }
        ),
    )

    company_name = forms.CharField(
        label="Наименование организации",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "companyName",
                "placeholder": "Наименование организации",
            }
        ),
    )

    inn = forms.CharField(
        label="ИНН",
        max_length=12,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inn",
                "placeholder": "ИНН",
            }
        ),
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"id": "message", "class": "form-control"}),
    )

    company_details = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "multiple": False,
                "allow_empty_file": True,
                "id": "company_details_input",
                "form": "cart_modal_form",
                "class": "form-control",
                "type": "file",
            }
        ),
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        correct_phone_number = PHONE_PATTERN
        if not re.match(correct_phone_number, phone_number.strip()):
            raise ValidationError("Проверьте правильно ли введен номер")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        correct_email = EMAIL_PATTERN
        if not re.match(correct_email, email):
            raise ValidationError(
                "Проверьте правильно ли указана почта для обратной связи"
            )
        return email
    

class CallForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "ФИО контактного лица",
                "class": "form-control",
                "id": "fullNameLegal",
            }
        ),
    )
    phone_number = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Номер телефона",
                "class": "form-control",
                "id": "validationPhoneNumber",
            }
        ),
    )
    
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"id": "message", "class": "form-control"}),
    )

    company_details = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "multiple": False,
                "allow_empty_file": True,
                "id": "company_details_input",
                "form": "cart_modal_form",
                "class": "form-control",
                "type": "file",
            }
        ),
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        correct_phone_number = PHONE_PATTERN
        if not re.match(correct_phone_number, phone_number.strip()):
            raise ValidationError("Проверьте правильно ли введен номер")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        correct_email = EMAIL_PATTERN
        if not re.match(correct_email, email):
            raise ValidationError(
                "Проверьте правильно ли указана почта для обратной связи"
            )
        return email
    
class ApplicationForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=120,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ваше имя",
                "class": "form-control",
                "id": "fullNameLegal",
            }
        ),
    )

    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@example.ru",
                "class": "form-control",
                "id": "email",
            }
        ),
    )
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        correct_phone_number = PHONE_PATTERN
        if not re.match(correct_phone_number, phone_number.strip()):
            raise ValidationError("Проверьте правильно ли введен номер")
        return phone_number

    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        correct_email = EMAIL_PATTERN
        if not re.match(correct_email, email):
            raise ValidationError(
                "Проверьте правильно ли указана почта для обратной связи"
            )
        return email