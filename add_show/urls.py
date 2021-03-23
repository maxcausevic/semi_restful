from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('add_show', views.add_show),
    path('results/<show_id>', views.display_result),
    path('all_shows_page', views.display_all_shows),
    path('delete/<show_id>', views.delete),
    path('show/<show_id>', views.display_result),
    path('edit/<show_id>', views.edit_page),
    path('update/<show_id>', views.update)
]