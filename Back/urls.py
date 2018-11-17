from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
#urls para poder llamar a funciones o clases 
#pido todos los url para poder hacer acciones en las views .
urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index,name="inicio"),
    url(r'^Usuarios/$',views.gestionarUsuarios,name="gestionarUsuarios"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^Nueva/$',views.MascotaCreate.as_view(),name="MascotaNueva"),
    url(r'^MostrarMascota/$',views.MascotaList.as_view(),name="MostrarMascota"),
    url(r'^MascotaUpdate/(?P<pk>\d+)/$',views.MascotaUpdate.as_view(),name="editarMascota"),
    url(r'^MascotaDelete/(?P<pk>\d+)/$',views.MascotaDelete.as_view(),name="MascotaDelete"),
    url(r'^Formulario/$',views.formulario,name="formulario"),
    url(r'^QuienesSomos/$',views.quienessomos,name="quienessomos"),
    url(r'^VerMascota/$',views.VerMascota,name="VerMascota"),
#introducimos urls para poder recuperar la contraseña por email cosa no muy facil
    url(r'^password_reset', PasswordResetView.as_view(), 
        {'template_name':'password_reset_form.html',
        'email_template_name': 'password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

