from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^myExp$',views.myexp),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist/(\d*)$',views.herolist),
    url(r'^area$',views.area),
    url(r'^area/(\d+)$',views.area2),
    url(r'^pr$',views.pr),
    url(r'^pro$',views.pro),
    url(r'^city(\d+)$',views.city),
    url(r'^htmlEditor$',views.htmlEditor),
    url(r'^htmlEditorHandle$',views.htmlEditorHandle),
    url(r'^content/$',views.htmlEditorHandle),
    url(r'^cache1$',views.cache1),
    url(r'^mysearch/$',views.mysearch),
    url(r'^celeryTest/$',views.celeryTest),
    ]