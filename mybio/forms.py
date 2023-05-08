from django import forms
from django.forms import Textarea

attr={'placeholder':'Please enter your message for me....',
    'style':'height:300px;width:600px;',
    
}

class MessageTable(forms.Form):
    message = forms.CharField(widget=Textarea(attrs=attr),
                               label=""
                               )
    