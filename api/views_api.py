from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from api.serializers import CutLinkSerializer
from api.base.response import CustomResponse
from django.shortcuts import get_object_or_404
from api.models import Link


class CustomCreateAPIView(CreateAPIView):
    """CustomCreateAPIView."""

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return CustomResponse(serializer.data, headers=headers).make_response()


class CutLinkAPIView(CustomCreateAPIView):
    """link - site url."""

    serializer_class = CutLinkSerializer
    queryset = Link.objects.all()


class GetAllStatisticsAPIView(APIView):
    """Return now site statistics."""

    def get(self, request, *args, **kwargs):
        models_count = Link.objects.all().count()
        response_data = {'count': models_count}
        return CustomResponse(response_data).make_response()


class GetLinkAPIView(APIView):
    """Return link statistics."""

    def get(self, request, *args, **kwargs):
        model = get_object_or_404(Link.objects.filter(key=kwargs['key']))
        response_data = {'passed': model.passed}
        return CustomResponse(response_data).make_response()
