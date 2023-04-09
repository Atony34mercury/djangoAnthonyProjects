from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Customer
from .forms import CustomerForm

# Create your views here.
def home_agenda(request,action):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            action = 'list' # Replace this with the parameter you want to pass.
            url = reverse('home_agenda', kwargs={'action': action})
            return redirect(url)
    else:
        form = CustomerForm()

    my_data = Customer.objects.all()
    show_element = "list"
    if not action is None:
        show_element = action
    return render(request, 'homeAgenda.html', {'my_data': my_data, 'show_element':show_element, 'form': form})