from django.conf.urls import url
from django.urls import path,include
from blogs import views


urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="blogs"),
    url(r'blogs/', views.HomeBlogsView.as_view(),name="blogs"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^blog/create/$', views.BlogCreate.as_view(success_url='/blogs/'), name='blog_create'),
    url(r'^blog/(?P<pk>\d+)/update/$', views.BlogUpdate.as_view(success_url='/blogs/'), name='blog_update'),
    url(r'^blog/(?P<pk>\d+)/delete/$', views.BlogDelete.as_view(success_url='/blogs/'), name='blog_delete'),
    url(r'^blog/(?P<pk>\d+)/$', views.DetallesBlogView.as_view(), name='blog_detalle')

]
