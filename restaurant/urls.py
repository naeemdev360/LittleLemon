from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("menu/",views.MenuItemsView.as_view(),name="menu view"),
    path("menu/<int:pk>",views.SingleMenuItemView.as_view(),name="singe menu view view"),
    path("booking/",views.BookingView.as_view(),name="booking view"),
    path("msg/",views.msg,name="message"),
    path("api-token-auth/",obtain_auth_token),
]