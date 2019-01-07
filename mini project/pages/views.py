from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail   import send_mail, get_connection
from . models import Page, Slider
from .forms import ContactForm
from . import actions
from background_task import background
from django.contrib.auth.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'slide': Slider.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)


def contact(request):

    context = {
        'page_list': Page.objects.all()
    }
    # assert False
    return render(request, 'pages/contact.html', context)

def stockView(request):
    action = actions.Actions()
    list2 = action.stocker()

    context = {
        'list2': list2,
        'page_list': Page.objects.all()
    }
    # assert False
    return render(request, 'pages/stock.html', context)



def wordCloud(request):
    new_years_2222 = datetime.datetime(2222, 1, 1)
    b_wordCloud(repeat=300, repeat_until=new_years_2222)
    context = {
        'page_list': Page.objects.all(),
        'slide': Slider.objects.all(),
    }
    return render(request, 'pages/cloud.html', context)

@background(schedule=5)
def b_wordCloud():
    action = actions.Actions()
    cloud = action.rssNewsHunter()
    context = {'cloud': cloud}
    return context
