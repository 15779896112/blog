import re
import views
urlpatterns = [
    (r'^$',views.index),
    (r'^login$',views.login),
    (r'^dologin$',views.doLogin),
    (r'^studentlist$',views.studentList),
    (r'^register$',views.register),
    (r'^static/',views.loadStatic),
    (r'^yzm',views.yzm),
]