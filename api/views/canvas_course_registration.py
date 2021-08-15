from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from api.serializers import CanvasCourseRegistrationSerializer
from canvas.models import CanvasCourseRegistration
from rest_framework.response import Response


class CanvasCourseRegistrationViewSet(viewsets.GenericViewSet,
                                      mixins.UpdateModelMixin,
                                      mixins.ListModelMixin,
                                      mixins.RetrieveModelMixin):
    """
    Optional Parameters
    - Base filtering on the 'course' parameter
    """
    serializer_class = CanvasCourseRegistrationSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['course', ]

    def get_queryset(self):
        return CanvasCourseRegistration.objects.order_by('user__id')

    def destroy(self, request, *args, **kwargs):
        reg = self.get_object()
        user = CanvasCourseRegistration.objects.get(id=reg.id)
        user.delete()
        return Response(status=204)
