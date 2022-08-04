from django.shortcuts import render


# Create your views here.
def snb_form(request):
    context = {}

    return render(request, 'snb_form.html', context=context)
