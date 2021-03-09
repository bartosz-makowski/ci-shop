from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """A view to render a customer's shopping bag """
    return render(request, 'bag/bag.html')