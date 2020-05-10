from . import views
from django.urls import include, path


urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:page>', views.page, name='page'),
    path('add/person', views.add_person, name='add_person'),
    path('memorial/<slug:person>', views.view_person, name='view_person'),
    path('accounts/', include('allauth.urls')),
]