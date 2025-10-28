from django import forms


class HousesFilterForm(forms.Form):
    min_price = forms.IntegerField(label='цена от', required=False)
    max_price = forms.IntegerField(label='цена до', required=False)
    query = forms.CharField(label='описание', required=False)
    ordering = forms.ChoiceField(label='сортировка', required=False, choices=[
        ('name', 'по алфавиту'),
        ('price', 'дешевле'),
        ('-price', 'дороже')
    ])