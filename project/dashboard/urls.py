from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/clientes', clientsViwSet, 'clientes')

router.register('api/proveedores', suppliersViwSet, 'proveedores')

router.register('api/productos', productsViwSet, 'productos')

urlpatterns = router.urls