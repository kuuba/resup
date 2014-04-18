from django.forms import ModelForm
from resup.models import Foo

class FooForm(ModelForm):
    class Meta:
        model = Foo
        fields = ['foo', 'bar']

