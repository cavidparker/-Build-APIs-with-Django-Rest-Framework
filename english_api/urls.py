from django.urls import path
# This one for a api_views
# from .api_views import WordList

#This one for generic views
# from . import generic_views 

# ## This one for viwsets
# from rest_framework import routers
# from . import viewset
# router = routers.DefaultRouter()
# router.register('english_api', viewset.WordViewSet)


## This one for mixins
from . import mixins
from rest_framework import routers

router = routers.DefaultRouter()
router.register('english_api', mixins.WordViewSet)

urlpatterns = [
    # This one for a api_views
    # path('words/', WordList.as_view(), name = 'word_list')

    #This one for generic views
    # path('', generic_views.ListCreateWord.as_view(), name='word_list'),
    # path('<int:pk>', generic_views.RetrieveUpdateDestroyWord.as_view(), name='word_detail'),
]
## this one for viewsets and mixins
urlpatterns += router.urls