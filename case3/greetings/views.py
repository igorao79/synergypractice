from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import NameForm
from .models import UserName


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            UserName.objects.create(name=name)
            messages.success(request, name)
            # Redirect after a successful save (Post/Redirect/Get) so
            # refreshing the page doesn't resubmit the form and create
            # a duplicate user.
            return redirect('index')
    else:
        form = NameForm()

    all_names = UserName.objects.all().order_by('-id')[:10]
    greeting = next(iter(messages.get_messages(request)), None)
    return render(request, 'greetings/index.html', {
        'form': form,
        'greeting': greeting,
        'names': all_names,
    })
