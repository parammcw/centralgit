from django.http import HttpResponse


from django.http import HttpResponse

def home_page(request):
    print("Home Page requested")
    return HttpResponse("This is home page")