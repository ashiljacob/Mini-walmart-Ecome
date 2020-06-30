from django.urls import path
from .views import HomePageView,delete,edit,save_item,add,add_item,bill_page,add_to_cart

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('delete/<int:id>/',delete,name='delete'),
    path('update/<int:id>/',edit,name='update'),
    path('save/<int:id>/',save_item,name='save'),
    path('add',add,name='add'),
    path('adding',add_item,name='add_item'),
    path('bill',bill_page,name='bill'),
    path('add_to_cart/<int:id>/',add_to_cart,name="add_to_cart"),

]