
from django.http import HttpResponse


def rectangle_area_params(request):
    try:
        height = int(request.GET.get('height'))
        width = int(request.GET.get('width'))
    except Exception:
        response = HttpResponse()
        response.status_code = 400
        response.reason_phrase = "Height and Width must be valid integers!"
        return response

    return HttpResponse(f'<h1>Rectangle area: {height * width}</h1>')


def rectangle_perimeter_params(request):
    try:
        height = int(request.GET.get('height'))
        width = int(request.GET.get('width'))
    except Exception:
        response = HttpResponse()
        response.status_code = 400
        response.reason_phrase = "Height and Width must be valid integers!"
        return response

    return HttpResponse(f'<h1>Rectangle perimeter: {2 * (height + width)}</h1>')


def circle_area_params(request):
    try:
        radius = int(request.GET.get('radius'))
    except Exception:
        response = HttpResponse()
        response.status_code = 400
        response.reason_phrase = "Radius must be a valid integer!"
        return response

    return HttpResponse(f'<h1>Circle area: {3.14 * radius ** 2}</h1>')


def circle_perimeter_params(request):
    try:
        radius = int(request.GET.get('radius'))
    except Exception:
        response = HttpResponse()
        response.status_code = 400
        response.reason_phrase = "Radius must be a valid integer!"
        return response

    return HttpResponse(f'<h1>Circle perimeter: {2 * 3.14 * radius}</h1>')


def rectangle_area(request, height, width):
    return HttpResponse(f'<h1>Rectangle area: {height * width}</h1>')


def rectangle_perimeter(request, height, width):
    return HttpResponse(f'<h1>Rectangle perimeter: {2 * (height + width)}</h1>')


def circle_area(request, radius):
    return HttpResponse(f'<h1>Circle area: {3.14 * radius ** 2}</h1>')


def circle_perimeter(request, radius):
    return HttpResponse(f'<h1>Circle perimeter: {2 * 3.14 * radius}</h1>')
