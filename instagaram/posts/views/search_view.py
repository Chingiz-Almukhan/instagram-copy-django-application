from django.db.models import Q
from django.shortcuts import render
from accounts.models import Account
from posts.forms import SearchForm


def search(request):
    accounts = []
    form = SearchForm
    if request.method == "POST":
        query = request.POST.get('search')
        if query == '':
            query = 'None'
        accounts = Account.objects.filter(
            Q(username__icontains=query) | Q(email__icontains=query) | Q(first_name__icontains=query))
    return render(request, 'search.html', {'accounts': accounts, 'form': form})
