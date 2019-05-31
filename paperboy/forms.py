from django import forms


class DeliveryForm(forms.Form):
    starting_house_number = forms.IntegerField()
    ending_house_number = forms.IntegerField()
