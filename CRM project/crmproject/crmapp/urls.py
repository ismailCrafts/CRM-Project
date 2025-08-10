from django.urls import path
from crmapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Home page - list or dashboard
    path('', views.home, name='home'),

    # User logout
    path('logout/', views.logout_user, name='logout'),

    # User registration page
    path('register/', views.register, name='register'),

    # View a single customer record by primary key (pk)
    path('record/<int:pk>', views.customer_record, name='record'),

    # Delete a customer record by primary key
    path('delete/<int:pk>', views.customer_delete, name='delete'),

    # Add a new customer record
    path('add_record/', views.add_record, name='add_record'),

    # Update an existing customer record by primary key
    path('update/<int:pk>', views.update_customer, name='update'),

    # Search customer records (GET request with query params)
    path('search/', views.search_results, name='search_results'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# Serve media files during development
