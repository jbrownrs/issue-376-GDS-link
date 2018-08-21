"""
Default URL patterns for the :py:mod:`ui` application are provided by the :py:mod:`.urls` module.
You can use the default mapping by adding the following to your global ``urlpatterns``:

.. code::

    from django.urls import path, include

    urlpatterns = [
        # ...
        path('', include('ui.urls')),
        # ...
    ]

"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'ui'

urlpatterns = [
    path(
        'media/new',
        login_required(TemplateView.as_view(template_name="ui/media_item_new.html")),
        name='media_item_new'
    ),
    path('media/<pk>/analytics', views.MediaItemAnalyticsView.as_view(),
         name='media_item_analytics'),
    path('media/<pk>/edit', views.MediaView.as_view(), name='media_item_edit'),
    path('media/<pk>', views.MediaView.as_view(), name='media_item'),
    path('channels/<pk>', views.ChannelView.as_view(), name='channel'),
    path(
        'playlists/new',
        login_required(TemplateView.as_view(template_name="ui/playlist_new.html")),
        name='playlist_new'
    ),
    path('playlists/<pk>', views.PlaylistView.as_view(), name='playlist'),
    path('playlists/<pk>/edit', views.PlaylistEditView.as_view(), name='playlist_edit'),
    path(
        'upload',
        login_required(TemplateView.as_view(template_name="ui/upload.html")),
        name='upload'
    ),
    path('about', TemplateView.as_view(template_name="ui/about.html"), name='about'),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
]
