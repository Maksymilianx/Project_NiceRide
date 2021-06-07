from django.urls import path

from NiceRide import views


urlpatterns = [
    path('add_offer/', views.SellCarView.as_view(), name='add_offer'),
    path('offers/', views.OffersView.as_view(), name='offers'),
    path('offers/<int:id>/', views.OfferDetailsView.as_view(), name='details'),
    path('offers_add_to_bookmarks/<int:id>/', views.OfferAddBookmarksView.as_view(), name='add_bookmarks'),
    path('bookmarks_list/', views.ShowBookmarksView.as_view(), name='bookmarks_list'),
    path('search/', views.AdvancedSearchView.as_view(), name='adv_search'),
    path('add_comment/', views.CommentView.as_view(), name='add_comment'),
    path('edit_comment/<int:pk>/', views.EditCommentView.as_view(), name='edit_comment'),
    path('edit_offer/<int:pk>/', views.EditOfferView.as_view(), name='edit_offer'),
    path('delete_offer/<int:pk>/', views.DeleteOfferView.as_view(), name='delete_offer'),
    path('send_message/', views.MessagesView.as_view(), name='send_message'),
    path('message_list/', views.ShowMessagesView.as_view(), name='message_list'),
    path('about/', views.AboutView.as_view(), name='about'),
]