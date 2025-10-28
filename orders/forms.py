from django import forms

from houses.models import House
from orders.models import Order


class OrderForm(forms.ModelForm):
    personal_data = forms.BooleanField(
        label='Я соглас(ен/на) на обработку персональных данных')
    house = forms.ModelChoiceField(queryset=House.objects.all(),
                                   widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ['house', 'name', 'phone']