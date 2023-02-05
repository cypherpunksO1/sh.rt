import datetime

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from api.serializers import CutLinkSerializer
from api.base.response import CustomResponse
from django.shortcuts import get_object_or_404
from api.models import Link, UniquePassed


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
        unique_passed = UniquePassed.objects.filter(link=model).count()
        response_data = {'passed': model.passed,
                         'unique_passed': unique_passed}
        return CustomResponse(response_data).make_response()


class GetLinkPassedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        link_model = get_object_or_404(Link.objects.filter(key=kwargs['key']))

        now_date = datetime.date.today()
        date_interval = now_date - datetime.timedelta(days=7)
        unique_passed_models = UniquePassed.objects.filter(created__gte=date_interval,
                                                           created__lte=now_date,
                                                           link=link_model)
        response_data = {}
        for unique_passed in unique_passed_models:
            created = str(unique_passed.created)
            if response_data.get(created):
                response_data[created] += 1
            else:
                response_data[created] = 1

        return CustomResponse(response_data).make_response()
