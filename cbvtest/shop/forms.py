from django import forms

from shop.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class FeedbackForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


    def send_message(self):
        # Метод якобы отсылает смс на email
        pass