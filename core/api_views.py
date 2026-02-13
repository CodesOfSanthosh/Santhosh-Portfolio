from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import ContactSerializer
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def contact_api(request):
    """
    API endpoint for contact form submission
    Accepts POST requests with name, email, subject, and message
    """
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'Your message has been sent successfully!'},
            status=status.HTTP_201_CREATED
        )
    logger.error(f"Contact API Validation Error: {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
