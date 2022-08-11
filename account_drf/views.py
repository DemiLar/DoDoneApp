from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from account.models import CustomizeUser
from .serializers import ProfileSerializer


class MyProfileViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CustomizeUser.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['work_position']
    search_fields = ['username']
    ordering_fields = ['-id']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(id=self.request.user.id)
        return query_set
