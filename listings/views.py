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
    queryset_list = Listing.objects.order_by('-list_date')

    # search by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = (
            queryset_list.filter(description__icontains=keywords) | 
            queryset_list.filter(county__iexact=keywords) | 
            queryset_list.filter(eircode__iexact=keywords) |
            queryset_list.filter(suburb__iexact=keywords)
            )
    
    # search by eircode
    if 'eircode' in request.GET:
        eircode = request.GET['eircode']
        if eircode:
            queryset_list = queryset_list.filter(eircode__iexact=eircode)
    
    # search by county
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county)

    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'county_choices': county_choices,
        'listings': paged_listings
    }
    return render(request, 'listings/search.html', context)
