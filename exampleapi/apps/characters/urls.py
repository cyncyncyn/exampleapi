from django.conf.urls import url
from .views import CharacterList, CharacterDetail

urlpatterns = [
    url(r'^$', CharacterList.as_view(), name='character-list'),
    url(r'^(?P<pk>\d+)/$', CharacterDetail.as_view(), name='character-detail'),
]
