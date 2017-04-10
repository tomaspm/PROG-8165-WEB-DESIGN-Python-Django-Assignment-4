from django.conf.urls import url
from AppTrans import views
# Template URLs
app_name="AppTrans"

urlpatterns = [

    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^category/$',views.category,name='category'),
    url(r'^transaction/$',views.transaction,name='transaction'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),

]
