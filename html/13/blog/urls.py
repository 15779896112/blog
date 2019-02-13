import re
import views
urlpatterns = [
    (r'^$',views.index),
    (r'^login$',views.login),
    (r'^dologin$',views.doLogin),
    (r'^studentlist$',views.studentList),
]