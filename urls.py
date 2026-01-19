from django.urls import path
from . import views

app_name = "links"

urlpatterns = urlpatterns = [
    path('', views.home, name="home"),
    path('add-platform/', views.add_platform, name="add_platform"),
    

    # Platform URLs
    path('platform/<slug:slug>/add-folder/', views.add_folder, name='add_folder'),
    path('platform/<slug:slug>/delete/', views.delete_platform, name="delete_platform"),
    path('platform/<slug:slug>/', views.platform_detail, name="platform_detail"),

    # Folder URLs
    path('folder/<int:id>/', views.folder_detail, name="folder_detail"),
    path('folder/<int:id>/add-link/', views.add_link, name="add_link"),
    path('folder/<int:id>/delete/', views.delete_folder, name="delete_folder"),

    # Link URLs
    path('link/<int:id>/delete/', views.delete_link, name="delete_link"),
    path('link/<int:id>/edit/', views.edit_link, name="edit_link"),
]

