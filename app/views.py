import random
from datetime import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        'current_date': now,
    }
    return render(request, 'app/index.html', context)


def select(request):
    context = {
        'number': 4
    }
    return render(request, 'app/select.html', context)


def result(request):
    chosen = int(request.GET['number'])

    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

    box = []

    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    results.sort()
    context = {
        'numbers': results
    }
    return render(request, 'app/result.html', context)