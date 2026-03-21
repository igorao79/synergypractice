from django.shortcuts import render
from .forms import NameForm
from .models import UserName


def index(request):
    greeting = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            UserName.objects.create(name=name)
            greeting = name
            form = NameForm()
    else:
        form = NameForm()

    all_names = UserName.objects.all().order_by('-id')[:10]
    return render(request, 'greetings/index.html', {
        'form': form,
        'greeting': greeting,
        'names': all_names,
    })
