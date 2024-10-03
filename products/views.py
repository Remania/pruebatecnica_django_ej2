from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Sobrescribir el método de creación
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        product_id = response.data.get('id')  # Obtener el ID del producto recién creado
        return Response({
            'message': f'Producto {product_id} creado correctamente.',
            'product': response.data
        }, status=status.HTTP_201_CREATED)

    # Sobrescribir el método de actualización (PUT completo)
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        product_id = response.data.get('id')  # Obtener el ID del producto actualizado
        return Response({
            'message': f'Producto {product_id} actualizado correctamente.',
            'product': response.data
        }, status=status.HTTP_200_OK)

    # Sobrescribir el método de eliminación
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()  # Obtener el objeto del producto
        product_id = product.id  # Obtener el ID del producto antes de eliminarlo
        super().destroy(request, *args, **kwargs)
        return Response({
            'message': f'Producto {product_id} eliminado correctamente.'
        }, status=status.HTTP_204_NO_CONTENT)

