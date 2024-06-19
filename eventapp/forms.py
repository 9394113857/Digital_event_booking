from django import forms
from eventapp.models import Customer,Eventmanager,Addevent,Administration,Bookevent,Review

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class AdministrationForm(forms.ModelForm):
    class Meta:
        model = Administration
        fields = "__all__"

class AddeventForm(forms.ModelForm):
    class Meta:
        model = Addevent
        fields = "__all__"

class EventmanagerForm(forms.ModelForm):
    class Meta:
        model = Eventmanager
        fields = ['title', 'email', 'password', 'mobile', 'address', 'city']


class AddeventForm(forms.ModelForm):
    class Meta:
        model = Addevent
        fields = "__all__"

class BookForm(forms.ModelForm):
    class Meta:
        model = Bookevent
        fields = ['customer','addevent','cost']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"