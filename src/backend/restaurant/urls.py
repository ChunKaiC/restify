
from xml.etree.ElementTree import Comment
from django.urls import path, include
from restaurant.views import AddImageView, ImageView, RemoveImageView, RestBlogView, SearchView
from restaurant.views import CommentRestaurantView, GetCommentsView
from restaurant.views import AddRestaurantView, EditRestaurantView, RestaurantView, MenuView, AddItemView, EditItemView

app_name = 'restaurant'  
  
urlpatterns = [
    path('<int:restaurant_id>/menu/', MenuView.as_view(), name='menu'),
    path('<int:restaurant_id>/menu/add/', AddItemView.as_view(), name='add'),
    path('menu/<int:pk>/edit/', EditItemView.as_view(), name='edit'),
    path('view/<int:pk>/', RestaurantView.as_view(), name='view_rest'),
    path('add/', AddRestaurantView.as_view(), name='add_restaurant'),
    path('edit/<int:pk>/', EditRestaurantView.as_view(), name='edit_restaurant'),
    path('<int:restaurant_id>/comment/', CommentRestaurantView.as_view(), name='comment'),
    path('<int:pk>/view/comments/', GetCommentsView.as_view(), name='get_comments'),
    path('search/', SearchView.as_view(), name='search'),
    path('<int:restaurant_id>/add/image/', AddImageView.as_view(), name='add_image'),
    path('remove/<int:pk>/image/', RemoveImageView.as_view(), name='remove_image'),
    path('<int:restaurant_id>/view/images/', ImageView.as_view(), name="view_image"),
    path('<int:restaurant_id>/blogs/', RestBlogView.as_view(), name='view_rest_blogs')
]