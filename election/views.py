from django.shortcuts import render

# Create your views here.
def pollingResult(request):
    return render(request, 'polling_unit_result.html')