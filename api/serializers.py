from rest_framework.serializers import ModelSerializer
from api.models import *
from api.base.tools import make_link_key


def convert_link(link: str) -> str:
    if 'https' not in link or 'http' not in link:
        link = 'https://' + link
    return link


class CutLinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = ('link', 'key')

    def create(self, validated_data):
        model = Link()
        model.link = convert_link(validated_data['link'])
        model.key = make_link_key()
        model.save()

        return model
