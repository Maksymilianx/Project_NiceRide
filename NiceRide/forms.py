from django import forms

from NiceRide.models import Car, Opinions, Messages


class OfferCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OpinionCreationForm(forms.ModelForm):
    class Meta:
        model = Opinions
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }


class MessageCreationForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['to_user', 'subject', 'content', 'date']
