from rest_framework import routers
from django.urls import re_path, path, include
from rest_framework.documentation import include_docs_urls
from .views import *
router = routers.DefaultRouter()
urlpatterns =[
    path(r'docs/', include_docs_urls(title='API Documentation')),
    
]

router.register(r'comments',CommentViewSet)
router.register(r'tickers',TickerViewSet)

urlpatterns+=router.urls