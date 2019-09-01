from django.shortcuts import render
from django.http import HttpResponseRedirect

from data.models import Post
from .forms import PostForm


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'data/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
            # record 를 생성하는 코드 필요
        return HttpResponseRedirect('/data/list/')

    form = PostForm()
    return render(request, 'data/create.html', {'form': form})


def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
        return render(request, 'data/confirm.html', {'form': form})
    return HttpResponseRedirect('/data/create/')
