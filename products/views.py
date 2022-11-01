from rest_framework import viewsets, mixins
from rest_framework.views import APIView

from products.models import ProductModel
from products.serializers import productSerializer
from .permissions import customPermission, superuserOrCreator
from .pagination import AdminPagination,UserPagination
from rest_framework import status
from rest_framework.response import Response

class MultiplePaginationMixin:
    def get_pagination_class(self):
            return self.pagination_class()
    
    @property
    def paginator(self):

        if not hasattr(self, '_paginator'):
            if self.get_pagination_class() is None:
                self._paginator = None
            else:
                self._paginator = self.get_pagination_class()
        return self._paginator

class productViewSet( mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = productSerializer
    permission_classes = (customPermission,)

    def get_queryset(self):
        queryset = ProductModel.objects.all()

        for item in self.request.GET:
            try:
                print({ item :self.request.GET[item] })
                queryset=queryset.filter(**{ item :self.request.GET[item] })
                print(queryset)
            except:
                if item =="ordering":
                    queryset=queryset.order_by(self.request.GET[item])
        return queryset

    def get_pagination_class(self):
        if self.request.user.is_superuser:
           return AdminPagination
        return UserPagination

    pagination_class = property(fget=get_pagination_class)


class noSaleProduct(APIView):
    permission_classes = (superuserOrCreator,)

    def delete(self, request, pk, format=None):
        try:
            instance = ProductModel.objects.get(pk=pk)
            self.check_object_permissions(self.request, instance)

            if instance.salesNumber == 0:
                instance.delete()
                message = {"message":f"product with id {pk} deleted"}
                return Response(message, status=status.HTTP_202_ACCEPTED)
        
            message = {"message":"NOT ALLOWED"}
            return Response(message, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except ProductModel.DoesNotExist:
            message = {"message":"NOT FOUND"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)


    
