from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Product
from .serializer import ProductSerializer  # Use .serializers if your file is named serializers.py
from rest_framework import generics
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    form = ProductForm()  # Ensure this is defined

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to refresh the page

    return render(request, 'keeru/home.html', {'products': products, 'form': form})

def about(request):
    return render(request, 'keeru/about.html')

def contact(request):
    return render(request, 'keeru/contact.html')

# REST API Views
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@require_POST
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('home')
