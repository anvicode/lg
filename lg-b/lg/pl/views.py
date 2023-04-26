from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return HttpResponse("Index page.")


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Category page {catid}</h1>")


def archive(request, year):
    if int(year) > 2022:
        return redirect("home")
    return HttpResponse(f"<h1>Archive page {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
