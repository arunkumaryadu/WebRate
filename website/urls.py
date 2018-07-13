from django.urls import include, path
from website import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views




urlpatterns = [

    path('', views.web_detail, name='home1'),
    path('', views.search_all, name='home2'),
    path('<int:wid>/',views.webView),
    path('<int:uid>/<int:wid>/',views.commentview),
    path('about/',views.about),
    path('contact/',views.contact),
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.web_detail, name='password_reset_complete'),


]+static(settings.STATIC_URL,document_root=settings.STATIC_DIR)
