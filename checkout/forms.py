from django import forms
from .models import BookingOrder

class BookingForm(frms.ModelForm):
    class Meta:
        model: BookingOrder
        fields = ('van', 'full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county', 'number_of_people', 'destination', 'daterange',)

    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'van': 'Van'
                'full_name': 'Full Name',
                'email': 'Email Address',
                'phone_number': 'Phone Number',
                'postcode': 'Postal Code',
                'town_or_city': 'Town or City',
                'street_address1': 'Street Address 1',
                'street_address2': 'Street Address 2',
                'county': 'County, State or Locality',
                'number_of_people': 'Number of People',
                'destination': 'Destination',
                'daterange': 'Dates'
            }

            self.fields['full_name'].widget.attrs['autofocus'] = True
            for field in self.fields:
                if field != 'country':
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
                