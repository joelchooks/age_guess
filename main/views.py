from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import get_cached_request_response
from .serializers import PersonNameSerializer


class HumanAgeView(APIView):
    """
    API endpoint to get age and date of birth based on the provided name.

    Requires a POST request with a JSON payload containing the name of the person.

    Returns a JSON response with the name, age, and date of birth of the person.
    If the request is invalid, returns a JSON response with error messages.
    """

    serializer_class = PersonNameSerializer

    @swagger_auto_schema(
        request_body=PersonNameSerializer,
        responses={
            status.HTTP_200_OK: openapi.Schema(type=openapi.TYPE_OBJECT),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                type=openapi.TYPE_OBJECT
            ),
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get("name")

        # Check if response is cached or request new data
        person_data = get_cached_request_response(name)
        response = {
            "name": person_data.get("name"),
            "age": person_data.get("age"),
            "date_of_birth": person_data.get("date_of_birth"),
        }
        return Response(response, status=status.HTTP_200_OK)
