from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # validation 필요
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입되었습니다"}, status=status.HTTP_201_CREATED)
        else: # 400 status code 사용 요청이 잘못 되었음을 알림
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
 # views.py에서 새로운 커스텀뷰를 상속을 받아서 작성
class CustomTokenObtainPairView(TokenObtainPairView):
    # serializer_class 새롭게 정의(generic? 알아서 자동화)
    serializer_class = CustomTokenObtainPairSerializer
