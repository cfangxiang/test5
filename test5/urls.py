"""test5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include,url
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'^',include('booktest.urls')),
#     url(r'^tinymce/',include('tinymce.urls')),
#     url(r'^search/',include('haystack.urls')),
# ]
l=[111,103,1,8,9,1,2,3,4,6,5,7,10,5,6,8,3,4,100]
l1=list(set(l))
l1.reverse()
print(l1,sorted(l1))