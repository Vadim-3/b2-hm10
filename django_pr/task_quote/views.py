from django.shortcuts import render
from .utils import get_mongodb


# Create your views here.


def main(request):
    db = get_mongodb()
    quotes = db.quotes.find()
    return render(request, 'task_quote/index.html', context={"task_quote": quotes})
