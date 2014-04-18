from resup.forms import FooForm

def upload(request):
    form = FooForm()
    return render(request, 'upload.html', {'form': form,})
