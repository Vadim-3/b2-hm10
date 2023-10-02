from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import TagForm, QuoteForm, AuthorForm
from .models import Tag, Author
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'task_quote/index.html', context={"task_quote": quotes_on_page})


def author_info(request, author_name):
    db = get_mongodb()
    author = db.authors.find_one({'name': author_name})
    return render(request, 'task_quote/author_info.html', context={"author": author})


@login_required
def upload_quotes(request):
    form = QuoteForm()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    db = get_mongodb()
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            tags = request.POST.getlist('tags')
            if tags:
                quote.tags.set(tags)
            return redirect(to='task_quote:root')
    return render(request, 'task_quote/upload_quotes.html', {'form': form, 'authors': authors, 'tags': tags})


@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='task_quote:root')
        else:
            return render(request, 'task_quote/tag.html', {'form': form})

    return render(request, 'task_quote/tag.html', {'form': TagForm()})


@login_required
def author(request):
    db = get_mongodb()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            db.authors.insert_one({
                'name': author.fullname,
                'born_date': author.born_date,
                'born_location': author.born_location,
                'description': author.description,
            })
            return redirect(to='task_quote:root')
    else:
        form = AuthorForm()

    return render(request, 'task_quote/author.html', {'form': form})
