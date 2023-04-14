from django import forms

class PlaceOrder(forms.Form):
    customerName = forms.CharField(label='Customer Name:', max_length=100, required=True) 