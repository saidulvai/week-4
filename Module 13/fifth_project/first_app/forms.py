from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    file = forms.FileField()
    email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICE = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices = CHOICE, widget=forms.RadioSelect)
    MEAL = [('p', 'Peparoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valName = self.cleaned_data['name']
#     #     if len(valName) < 10:
#     #         raise forms.ValidationError("Enter a name wirh at least 10 characters")
#     #     else:
#     #         return valName
        
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valemail

#     def clean(self):
#         clean_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name wirh at least 10 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")
    
class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message="Enter a name with at least 10 characters")])
    email = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MinValueValidator(24, message="age must at least 24"), validators.MaxValueValidator(34, message="Age must be maximum 34")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="File extension must be ended .pdf")])

class PasswordValidationproject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']

        if val_conpass != val_pass:
            raise forms.ValidationError("password does not match!")
        if len(val_name) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")
