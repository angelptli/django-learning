"""django_learning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . views import dimsum_detail_view, add_item_view

app_name = 'dim_sum'
urlpatterns = [
    path('add_item/', add_item_view, name='add_item_view'),
    path('detail/', dimsum_detail_view, name="dimsum_detail_view"),
    # path('<int:id>/', dimsum_lookup_view, name='dimsum_lookup')
]
