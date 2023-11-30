from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name='moviepost'
urlpatterns=[
    path('posted/',
         views.PostedView.as_view(),
         name='posted'),
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_success'),
    path('usercontents/',
         views.UsercontentsView.as_view(),
         name='usercontents'),
    
     path('usercontents/<int:category>',
         views.UsercontentsmainView.as_view(),
         name = 'usercontents_main'
         ),
     
     path('posted/<int:pk>/delete/',
     views.MovieDeleteView.as_view(),
     name='delete'),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)