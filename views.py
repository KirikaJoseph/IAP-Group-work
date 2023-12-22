
from django.shortcuts import render, redirect
from .forms import UserFeedbackForm

def feedback_form(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserFeedbackForm()

    return render(request, 'main/feedback_form.html', {'form': form})

def feedback_success(request):
    return render(request, 'main/feedback_success.html')
