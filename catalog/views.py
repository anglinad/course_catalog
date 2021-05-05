from django.shortcuts import render, get_object_or_404

from .forms import SearchForm
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request,
                  'catalog/course/list.html',
                  {'courses': courses})


def course_detail(request, course_id, slug):
    course = get_object_or_404(Course,
                               id=course_id,
                               slug=slug)
    return render(request,
                  'catalog/course/detail.html',
                  {'course': course})


def course_search(request):
    form = SearchForm()
    query = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.data['query']
    results = Course.objects.filter(name__icontains=query) if query else []
    return render(request, 'catalog/course/search.html', {'form': form,
                                                          'query': query,
                                                          'results': results})
