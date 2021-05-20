from django.shortcuts import render, redirect
import requests
from .forms import *

http_code = {
    100: "Continue", 101: "Switching Protocols", 103: "Checkpoint",
    200: "OK", 201: "Created", 202: "Accepted", 203: "Non-Authoritative Information", 204: "No Content", 205: "Reset Content", 206: "Partial Content",
    300: "Multiple Choices", 301: "The Requested Page has moved permanently to a new URL", 302: "The Requested Page has moved temporarily to a new URL", 303: "The Requested Page can be found under a different URL", 304: "Not Modified", 306: "Switch Proxy: No longer used",
    400: "Bad Request", 401: "Unauthorized", 402: "Payment required", 403: "Forbidden", 404: "Not Found", 408: "Request Timeout",
    500: "Internal Server Error", 501: "Not Implemented", 502: "Bad Gateway", 503: "Service Unavailable", 504: "Gateway Timeout"
}
# Create your views here.


def home(request):
    return render(request, 'home.html')


def status(request):
    url = request.POST['url']
    if url[:4] != "http" and url[:3] == "www":
        url = "https://" + url
    elif url[:4] != "http" and url[:3] != "www":
        return render(request, "home.html", {'url': url, 'message': "Invalid URL"})

    try:
        source = requests.get(url)
    except:
        return render(request, "home.html", {'url': url, 'message': "The Site can't be reached."})
    for key in http_code.keys():
        if source.status_code == key:
            if key == 100 or key == 200 or key == 201 or key == 202:
                count = 1
                return render(request, "home.html", {'url': url, 'count': count, 'message': http_code[key]})
            else:
                count = 1
                return render(request, "home.html", {'url': url, 'count': count, 'message': http_code[key]})


def multiple(request):

    form = URLForm()

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            form = URLForm()

    url_list = URLS.objects.all()

    result = []
    for details in url_list:
        url = str(details.URL)
        if url[:4] != "http" and url[:3] == "www":
            url = "https://" + url
        elif url[:4] != "http" and url[:3] != "www":
            result.append("Invalid URL")

        try:
            source = requests.get(url)
        except:
            result.append("The Site can't be reached.")
        for key in http_code.keys():
            if source.status_code == key:
                if key == 100 or key == 200 or key == 201 or key == 202:
                    result.append(http_code[key])
                else:
                    result.append(http_code[key])

    Detail = zip(url_list, result)

    return render(request, 'multiple.html', {'form': form, 'url_list': url_list, 'Detail': Detail})


def urldeleteform(request, pk):

    url_list = URLS.objects.get(id=pk)
    url_list.delete()

    return redirect('multiple')
