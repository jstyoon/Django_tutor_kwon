from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    return Response("연결되었습니다!")