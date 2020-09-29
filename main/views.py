from django.shortcuts import render

from main.forms import UserForm


def user_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'thanks_page.html')
    else:
        form = UserForm()
    return render(request, 'main_page.html', {'form': form})

