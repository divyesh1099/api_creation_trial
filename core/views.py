from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Post
# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post

# Create your views here.
class TestView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(request, *args, **kwargs):
        qs = Post.objects.all()
        post = qs.first()
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(request, *args, **kwargs):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# def test_view(request):
#     data = {
#         'name': 'Moti',
#         'last_name': 'Vation',
#         'DOB': '07/06/00',
#         'Ph_No': 1234567890
#     }
#     return JsonResponse(data) # Pass safe = False if you want to pass a list