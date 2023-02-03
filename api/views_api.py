from rest_framework.views import APIView
from api.serializers import CutLinkSerializer
from api.base.response import CustomResponse

from rest_framework.generics import CreateAPIView

from api.models import *


class CutLinkAPIView(APIView):
    """
    link - полная ссылка на сайт
    """

    def post(self, request, *args, **kwargs):
        serializer = CutLinkSerializer(data=request.data)

        if serializer.is_valid():
            model = serializer.create(serializer.validated_data)
            return CustomResponse({'key': model.key,
                                   'link': model.link}).good()
        else:
            return CustomResponse(serializer.errors).bad()


class GetAllStatisticsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        models_count = Link.objects.all().count()
        data = {
            'links': {
                'count': models_count
            }
        }
        return CustomResponse(data).good()


class GetLinkAPIView(APIView):
    def get(self, request, *args, **kwargs):
        model = Link.objects.filter(key=kwargs['key'])
        if model:
            model = model[0]
            data = {
                'link': model.link,
                'passed': model.passed,
                'unique_passed': model.unique_passed.all().count()
            }
            return CustomResponse(data).good()
        else:
            return CustomResponse({}).bad_404()
