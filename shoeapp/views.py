from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserCreationForm, UserSigninForm, BrandModelForm, ProductCreateForm
from .models import User, Brand,Product,Cart
#
# def index(request):
#     return render(request, "index.html")

def index(request):
    return render(request, "index.html")

def create_brand(request):
    form = BrandModelForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = BrandModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "createbrand.html", context)

#
# def update_brand(request, id):
#     brand = Brand.objects.get(id=id)
#     form = BrandModelForm(instance=brand)
#     context = {}
#     context["form"] = form
#     if request.method == "POST":
#         form = BrandModelForm(instance=brand, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("list")
#     return render(request, "update.html", context)
#
#
# def delete_brand(request, id):
#     brand = Brand.objects.get(id=id)
#     brand.delete()
#     return redirect("list")
#
#
# def list_all(request):
#     brands = Brand.objects.all()
#     context = {}
#     context["brands"] = brands
#     return render(request, "list.html", context)
#
#
# def product_create(request):
#     form = ProductCreateForm()
#     context = {}
#     context["form"] = form
#     if request.method == "POST":
#         form = ProductCreateForm(request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("fetchitems")
#         else:
#             context["form"] = form
#             return render(request, "productdetail.html", context)
#
#
#     return render(request, "productdetail.html", context)
#
#
# def list_products(request):
#     mobiles = Product.objects.all()
#     context = {}
#     context["mobiles"] = mobiles
#     return render(request, "listproduct.html", context)
#
#
# def get_object(id):
#     return Product.objects.get(id=id)
#
#
# def edit_item(request, *args, **kwargs):
#     id = kwargs.get("id")
#     product = get_object(id)
#     form = ProductCreateForm(instance=product)
#     context = {}
#     context["form"] = form
#     if request.method == "POST":
#         form = ProductCreateForm(instance=product, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("fetchitems")
#     return render(request, "edit_product.html", context)
#
#
# def detail_product(request, *args, **kwargs):
#     id = kwargs.get("id")
#     product = get_object(id)
#     context = {}
#     context["product"] = product
#     return render(request, "detail_product.html", context)
#
#
# def delete_product(request, *args, **kwargs):
#     id = kwargs.get("id")
#     product = get_object(id)
#     product.delete()
#     return redirect("fetchitems")
