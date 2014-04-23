from resup.forms import FooForm
from django.shortcuts import render

def upload(request):
    form = FooForm()
    return render(request, 'upload.html', {'form': form,})
