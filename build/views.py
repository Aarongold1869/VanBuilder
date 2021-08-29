from django.shortcuts import render

# Create your views here.

def build_list_view(request, *args, **kwargs):
    return render(request, "builds/build-list.html")