from rest_framework.response import Response
from rest_framework import status


class CustomResponse:
    def __init__(self, data: dict, message: str = None, **kwargs):
        self.data = data
        self.message = message
        self.kwargs = kwargs

    def make_response(self, error: bool = False) -> Response:
        data = {
            'error': error,
            'message': self.message,
            'data': self.data
        }

        _status = status.HTTP_200_OK

        if error:
            _status = status.HTTP_400_BAD_REQUEST

        return Response(
            data=data,
            status=_status,
            **self.kwargs
        )


class CustomErrors:
    def __init__(self, field: str):
        self.field = field

    def object_not_found_error(self) -> dict:
        return {self.field: ['Объекта не существует.']}

    def object_already_exists_error(self):
        return {self.field: ['Объект с такими параметрами уже существует.']}

    def no_permission_error(self):
        return {self.field: ['Недостаточно прав доступа.']}
