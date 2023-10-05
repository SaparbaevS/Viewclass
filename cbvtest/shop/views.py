from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView, UpdateView, DeleteView

from shop.forms import FeedbackForm, ProductModelForm
from shop.models import Product


class StartPageView(TemplateView):
    template_name = 'start_page.html'


class FeedbackView(FormView):
    template_name = 'feedback_page.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('start_page')

    def post(self, request, *args, **kwargs):
        # Обработка Post запрос
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Обработка Get запрос
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.send_message()
        return super().form_valid(form)

# def show_products(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "show_product.html", context)

class ProductListView(ListView):
    model = Product
    template_name = 'show_product.html'
    context_object_name = "products"


# def product_detail(request, slug_param):
#     product = get_object_or_404(Product, slug=slug_param)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'

# def add_product(request):
#     form = modelform_factory(Product, fields="__all__")
#     if request.method == "POST":
#         data = form(request.POST)
#         if data.is_valid():
#             data.save()
#             return redirect("show_products")
#         else:
#             return render(request, "add_product.html", {'form': data})
#
#     else:
#         context = {"form": form}
#         return render(request, "add_product.html", context)





class AddProductView(CreateView):
    model = Product
    form_class = modelform_factory(Product, fields="__all__")
    template_name = "add_product.html"
    success_url = reverse_lazy("show_products")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'update_product.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy("show_products")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy("show_products")

