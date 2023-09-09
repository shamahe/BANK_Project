from django import forms
from django.conf import Settings, settings
from django.forms import DateField
from django.http import request

from .models import  Branch, Person

MATERIAL_CHOICES = (
    ('debitcard', 'Debit Card'),
    ('creditcard', 'Credit Card'),
    ('chequebook', 'Cheque Book'),)


class PersonForm(forms.ModelForm):
    materialrequired = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 choices=MATERIAL_CHOICES)

    class Meta:
        model = Person
        # birthdate = DateField(input_formats=settings.DATE_INPUT_FORMATS)
        fields = ('name', 'birthdate', 'age', 'gender','phone_number','email_id','address', 'account_type', 'district', 'branch', 'materialrequired')
        # birthdate = DateField(input_formats=['%Y-%m-%d'])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birthdate'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        # self.fields['birthdate'].widget = forms.widgets.DateInput(
        #     attrs={
        #         'type': 'date', 'placeholder': 'enter the dob '
        #         # 'class': 'form-control'
        #     }
        # )

        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')

    # def clean(self):
    #     cleaned_data = super(PersonForm, self).clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
    #     message = cleaned_data.get('message')
    #     if not name and not email and not message:
    #         raise forms.ValidationError('You have to write something!')