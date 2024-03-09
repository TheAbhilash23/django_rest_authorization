from rest_framework import routers

from test_app_1 import views as test_app_1_views
from test_app_2 import views as test_app_2_views
from test_app_3 import views as test_app_3_views

router = routers.SimpleRouter()
# router = routers.DefaultRouter()

router.register(
    r'test_app_1_car', test_app_1_views.CarModelView,
    basename="test_app_1_car_model")
router.register(
    r'test_app_1_book', test_app_1_views.BookCategoryView,
    basename="test_app_1_book")
router.register(
    r'test_app_2_restaurant_menu', test_app_2_views.RestaurantMenuView,
    basename="test_app_2_restaurant_menu")
router.register(
    r'test_app_2_movie_genre', test_app_2_views.MovieGenreView,
    basename="test_app_2_movie_genre")
router.register(
    r'test_app_3_event_schedule', test_app_3_views.EventScheduleView,
    basename="test_app_3_event_schedule")
router.register(
    r'test_app_3_product_category_view', test_app_3_views.ProductCategoryView,
    basename="test_app_3_product_category_view")
