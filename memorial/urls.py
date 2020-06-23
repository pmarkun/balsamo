from . import views
from django.urls import include, path

#app_name = 'balsamo'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<slug:page>', views.page, name='page'),
    path('add/person', views.add_person, name='add_person'),
    path('memorial/<slug:person>', views.view_person, name='view_person'),
    path('memorial/delete/<int:pk>', views.MemoryDelete.as_view(), name='memory_delete'),
    #path('accounts/', include(('allauth.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include('allauth.urls')),
]