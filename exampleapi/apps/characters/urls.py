from django.conf.urls import url
from .views import CharacterList, CharacterDetail, PhotoList, PhotoDetail

urlpatterns = [
    url(r'^$', CharacterList.as_view(), name='character-list'),
    url(r'^(?P<pk>\d+)/$', CharacterDetail.as_view(), name='character-detail'),
    url(r'^photos/$', PhotoList.as_view(), name='photo-list'),
    url(r'^photos/(?P<pk>\d+)/$', PhotoDetail.as_view(), name='photo-detail'),
]
