from django.urls import path
from . import views
urlpatterns = [
    
    # /hoge に 対応
    
    path('', views.index),
    
    # /hoge/ foo に 対応
    
    path('foo', views.foo),
    
    # /hoge/ woo に 対応
    
    path('woo', views.woo), 
]
