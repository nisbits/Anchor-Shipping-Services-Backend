from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer


@api_view(['GET', 'POST'])
def review_list(request):
    """
    GET: Retrieve all reviews
    POST: Create a new review
    """
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
