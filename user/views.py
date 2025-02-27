from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Create user but do not log in
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }

    return render(request, "registration/register.html", context)
