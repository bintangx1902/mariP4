from django.urls import path
from .views import *

app_name = 'read'

urlpatterns = [
    path('', AllBooksList.as_view(), name='book'),
    path('book/', AllBookList.as_view(), name='book-list'),
    # path('<str:cats>/', CategorySearch, name='category'),
    path('<slug:link>/', BookDetailView.as_view(), name='detail'),
    path('<slug:link>/comment/', AddComment.as_view(), name='add-comment'),
]
