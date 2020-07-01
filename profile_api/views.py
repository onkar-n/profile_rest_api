from rest_framework.views import APIView
from rest_framework.response import Response

class helloApiView (APIView):

    def get(self, request, format=None):
        api_view = ['get', 'push', 'delete']
        return Response({'message':'Hello', 'item':api_view})
