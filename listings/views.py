from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import county_choices, bedroom_choices, price_choices

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
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    """ View to render Search template """
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices
    }
    return render(request, 'listings/search.html', context)
