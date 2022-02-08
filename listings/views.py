from django.shortcuts import render

def index(request):
    """ View to render template displaying all listings """
    return render(request, 'listings/listings.html')


def listing(request):
    """ View to render template displaying individual home listing """
    return render(request, 'listings/listing.html')


def search(request):
    """ View to render Search template """
    return render(request, 'listings/search.html')
