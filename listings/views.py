from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

def index(request):
    """ View to render template displaying all listings """
    # listings = Listing.objects.all() for all listings
    # listings should be ordered based on date added, and only display listings if is_published is True
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #6 listings per page
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """ View to render template displaying individual home listing """
    return render(request, 'listings/listing.html')


def search(request):
    """ View to render Search template """
    return render(request, 'listings/search.html')
