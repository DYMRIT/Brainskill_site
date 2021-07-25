from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DeleteView
from courses.models import Course, BaseForArticle, Homework
from telegrambots.forms import OrderForm
from telegrambots.sendmessage import sendTelegram


class CourseListView(ListView):
    paginate_by = 5
    model = Course
    template_name = 'courses/home_page.html'


def price(request):
    return render(request, 'price.html')


def about(request):
    return render(request, 'about.html')


def help_us(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            username = request.user.username
            title = request.POST['title']
            text = request.POST['text']
            form.save()
            sendTelegram(username, title, text)
    form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'help_us.html', context)


#@permission_required('homework.view', login_url='/')
def sale(request):
    return render(request, 'sale.html')


@login_required
def detail_course(request, slug_course):
    course = Course.objects.filter(slug_course=slug_course).first()
    articles = course.bind_course_set.all()
    context = {
        'articles': articles,
        'slug_course': slug_course,
    }
    return render(request, 'courses/detail.html', context)


@login_required
def month(request, slug, slug_article):
    article = BaseForArticle.objects.filter(slug_article=slug_article).first()
    homeworks = article.bind_month_set.all()
    lst = Paginator(homeworks, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    time_now = timezone.now()
    context = {
        'time_now': time_now,
        'article': article,
        'slug_course': slug,
        'slug_article': slug_article,
        'page_obj': page_obj,
    }
    return render(request, 'courses/month.html', context)