from django.urls import path
from .views import (
    main_view,
    main_view2,
    main_view3,
    main_view4,
    move_func,
    get_matrix,
    jacobi_api,
)

app_name = "robot"

urlpatterns = [
    # SERVICES
    path("", main_view, name="main-view"),
    path("test2/", main_view2, name="main-view2"),
    path("test3/", main_view3, name="main-view3"),
    path("test4/", main_view4, name="main-view4"),
    path("api/move/", move_func, name="move"),
    path("api/matrix/", get_matrix, name="matrix"),
    path("api/jacobian/", jacobi_api, name="jacobi_api"),
]
