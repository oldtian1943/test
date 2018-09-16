from django.conf.urls import url
from .import views

app_name='[blogs]'
urlpatterns=[
        url(r'^$',views.home,name='home'),
        url(r'^home/(?P<post_id>\d+)/$',views.post,name='post'),
        url(r'^add_post/$',views.add_post,name='add_post'),
        url(r'^edit_post/(?P<post_id>\d+)/$',views.edit_post,name='edit_post'),
        ]