from django.urls import path
from django.views.generic import RedirectView

from .views import ReflectedHTMLView, ReflectedJSONView, ReflectedURLView, ReflectedURLSchemeView

app_name = 'reflected0'
urlpatterns = [
    path('', RedirectView.as_view(pattern_name="reflected0:simple"), name='index'),
    path('/simple', ReflectedHTMLView.as_view(), name='simple'),
    path('/json', ReflectedJSONView.as_view(), name='json'),
    path('/url', ReflectedURLView.as_view(), name='url'),
    path('/url-scheme', ReflectedURLSchemeView.as_view(), name='url-scheme'),
]
