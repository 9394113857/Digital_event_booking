"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from eventapp import views as v
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('about/', v.about, name="about"),
    path('contact/', v.contact, name="contact"),

# Customer urls
    path('customer/', v.customer, name="customer"),
    path('customer_login/', v.customer_login, name="customer_login"),
    path('regpage/', v.regpage, name="regpage"),
    path('reg/', v.reg, name="reg"),
    path('customer_change/', v.customer_change, name="customer_change"),
    path('customer_display/', v.customer_display, name="customer_display"),
    path('customer_update/', v.customer_update, name="customer_update"),
    path('customer_viewevent/', v.customer_viewevent, name="customer_viewevent"),
    path('customer_viewbook/', v.customer_viewbook, name="customer_viewbook"),
    path('customer_viewreview/<int:id>', v.customer_viewreview, name="customer_viewreview"),
    path('customer_delete/<int:id>', v.customer_delete, name="customer_delete"),
    path('customer_edit/<int:id>', v.customer_edit, name="customer_edit"),
    path('customer_logout/', v.customer_logout, name="customer_logout"),
    path('customerhome/', v.customerhome, name="customerhome"),
    path('eventmanagerhome/', v.eventmanagerhome, name="eventmanagerhome"),
    path('cancel_book/<str:booking_id>', v.cancel_book, name="cancel_book"),



# Eventmanager urls
    path('eventmanager/', v.eventmanager, name="eventmanager"),
    path('customer_bookings/', v.customer_bookings, name="customer_bookings"),
    path('eventmanager_login/', v.eventmanager_login, name="eventmanager_login"),
    path('eventmanager_logout/', v.eventmanager_logout, name="eventmanager_logout"),
    path('eventmanager_registerpage/', v.eventmanager_registerpage, name="eventmanager_registerpage"),
    path('eventmanager_reg/', v.eventmanager_reg, name="eventmanager_reg"),
    path('eventmanager_change/', v.eventmanager_change, name="eventmanager_change"),
    path('eventmanager_display/', v.eventmanager_display, name="eventmanager_display"),
    path('eventmanager_viewevent/', v.eventmanager_viewevent, name="eventmanager_viewevent"),
    path('post_event/', v.post_event, name="post_event"),

    path('eventmanager_viewreview/<int:id>', v.eventmanager_viewreview, name="eventmanager_viewreview"),
    path('eventmanager_viewbook/<int:id>', v.eventmanager_viewbook, name="eventmanager_viewbook"),
    path('add_event/', v.add_event, name="add_event"),
    path('view_event/', v.view_event, name="view_event"),
    path('addevent_edit/<int:id>', v.addevent_edit, name="addevent_edit"),
    path('addevent_delete/<int:id>', v.addevent_delete, name="addevent_delete"),
    path('addevent_update/', v.addevent_update, name="addevent_update"),
    path('eventmanager_edit/<int:id>', v.eventmanager_edit, name="eventmanager_edit"),
    path('manager_edit/<int:id>', v.manager_edit, name="manager_edit"),
    path('manager_update/', v.manager_update, name="manager_update"),
    path('accept_book/<str:booking_id>', v.accept_book, name="accept_book"),
    path('reject_book/<str:booking_id>', v.reject_book, name="reject_book"),

    # Admin urls
    path('administration/', v.administration, name="administration"),
    path('admin_login/', v.admin_login, name="admin_login"),
    path('admin_viewevent/', v.admin_viewevent, name="admin_viewevent"),
    path('admin_viewreview/', v.admin_viewreview, name="admin_viewreview"),
    path('admin_logout/', v.admin_logout, name="admin_logout"),
    path('book/<int:id>', v.book, name="book"),
    path('admin_viewbook/', v.admin_viewbook, name="admin_viewbook"),
    path('admin_viewcustomer/', v.admin_viewcustomer, name="admin_viewcustomer"),
    path('admin_viewcontact/', v.admin_viewcontact, name="admin_viewcontact"),
    path('administrationhome/', v.administrationhome, name="administrationhome"),
    path('admin_vieweventmanager/', v.admin_vieweventmanager, name="admin_vieweventmanager"),

    path('review/<int:id>', v.review, name="review"),
    path('Admin_customer_delete/<int:id>', v.Admin_customer_delete, name="Admin_customer_delete"),
    path('Admin_manager_delete/<int:id>', v.Admin_manager_delete, name="Admin_manager_delete"),
    path('Admin_event_delete/<int:id>', v.Admin_event_delete, name="Admin_event_delete"),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)