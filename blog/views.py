from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseNotFound
from django.conf import settings


def blog(request, page):
    blogs = Blog.objects.all().order_by("-pk")
    paginator = Paginator(blogs, settings.ARTICLE_PAGINATE_BY)  

    try:
        current_page = paginator.page(page)
    except:
        return HttpResponseNotFound('<h1>404 page Not Found</h1>')

    context = {
        "current": page,
        "current_page": current_page,
        "paginator": paginator,
    }
    return render(request, 'blog/blog.html', context)

def blog_pagination(request, page):
    blogs = Blog.objects.all().order_by("-pk")
    paginator = Paginator(blogs, settings.ARTICLE_PAGINATE_BY)

    try:
        page = paginator.page(page)
    except:
        return JsonResponse({'blogs':[],'has_next':None}, status=404)

    has_next = page.has_next()

    objects = [blog.get_json() for blog in page.object_list]
    context = {
        "blogs": objects,
        "has_next": has_next
    }

    return JsonResponse(context)


def single_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/single.html', {'blog': blog})
