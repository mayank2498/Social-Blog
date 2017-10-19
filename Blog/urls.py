from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.blog,name="blog"),
    url(r'^add$',views.add_blog,name="add_blog"),
    url(r'^approve/(?P<blog_id>[0-9]+)$',views.approve_blog,name="approve_blog"),
    url(r'^(?P<blog_id>[0-9]+)$',views.blog_full,name="blog_full")

]