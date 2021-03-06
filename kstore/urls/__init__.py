#encoding:utf-8
from django.conf.urls import include, url

from kstore.views import ManageIndexView

urlpatterns = [
    url(r'^$', ManageIndexView.as_view(), name='index'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^user/', include('user_profile.urls', namespace='userprofile')),
    url(r'^products/', include('kstore.urls.products', namespace='products')),
    url(r'^blog/', include('kblog.urls.blogmanager', namespace='blog-manager')),
    url(r'^mail/', include('kstore_mail.urls.mail', namespace='mail')),
]
