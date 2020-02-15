
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SimpleForm
import logging

logger = logging.getLogger(__name__)

def myform(request):
    form = SimpleForm()
    content = request.POST.get('content')
    logger.debug(content)
    return render(request, 'ex02/form.html', {'myform': form})


def index(request):
    return render(request, 'ex02/index.html', {})

