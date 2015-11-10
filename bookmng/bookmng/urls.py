from django.conf.urls import patterns, include, url
from bookmng import settings
from django.contrib import admin
from books import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookmng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^search/$', views.search),
    (r'^book_info/$', views.book_info),
    (r'^delete/$', views.del_a_book),
#    (r'^add_book/$', views.add_book),
#    (r'^add_author/$', views.add_author),
    (r'^static/(P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL, 'show_indexes': True}),
)
