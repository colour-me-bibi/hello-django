
from django.http import HttpResponse


def rectangle_area_params(request):
    # get height and width from url parameters
    height = int(request.GET.get('height'))
    width = int(request.GET.get('width'))

    return HttpResponse(f'Rectangle area: {height * width}')


def rectangle_perimeter_params(request):
    height = int(request.GET.get('height'))
    width = int(request.GET.get('width'))

    return HttpResponse(f'Rectangle perimeter: {2 * (height + width)}')


def circle_area_params(request):
    radius = int(request.GET.get('radius'))

    return HttpResponse(f'Circle area: {3.14 * radius ** 2}')


def circle_perimeter_params(request):
    radius = int(request.GET.get('radius'))

    return HttpResponse(f'Circle perimeter: {2 * 3.14 * radius}')


def rectangle_area(request, height, width):
    return HttpResponse(f'Rectangle area: {height * width}')


def rectangle_perimeter(request, height, width):
    return HttpResponse(f'Rectangle perimeter: {2 * (height + width)}')


def circle_area(request, radius):
    return HttpResponse(f'Circle area: {3.14 * radius ** 2}')


def circle_perimeter(request, radius):
    return HttpResponse(f'Circle perimeter: {2 * 3.14 * radius}')
