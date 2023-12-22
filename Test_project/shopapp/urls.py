"""
URL configuration for Test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import main, CreateItem, ItemDetailsView, buy

urlpatterns = [
        path("main/", main, name='main'),
        path("create_item/", CreateItem.as_view(), name="create_item"),
        path('item/<int:pk>', ItemDetailsView.as_view(), name="item_details"),
        path('buy/<int:id>', buy, name="buy_item"),
]
