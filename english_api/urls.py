from django.urls import path
# This one for a api_views
# from .api_views import WordList

#This one for generic views
# from . import generic_views 

from rest_framework import routers
from . import viewset

router = routers.DefaultRouter()
router.register('english_api', viewset.WordViewSet)

urlpatterns = [
    # This one for a api_views
    # path('words/', WordList.as_view(), name = 'word_list')

    #This one for generic views
    # path('', generic_views.ListCreateWord.as_view(), name='word_list'),
    # path('<int:pk>', generic_views.RetrieveUpdateDestroyWord.as_view(), name='word_detail'),
]

urlpatterns += router.urls