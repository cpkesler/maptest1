from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from tethys_sdk.gizmos import RangeSlider


@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    # slider1 = RangeSlider(display_text='Slider 1',
    #                       name='slider1',
    #                       min=0,
    #                       max=100,
    #                       initial=50,
    #                       step=1)
    context = {}

    return render(request, 'maptest1/home.html', context)