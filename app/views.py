from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import UserInfo
from app.serializer import UserInfoSerializer


# Create your views here.

@api_view(["POST"])
def create_game(request):
    serializer = UserInfoSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "username": user.username,
            "name": user.name,
            "surname": user.surname,
            "age": user.age,
            "birthday": user.birthday,
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_games(request):
    games = UserInfo.objects.all()
    serializer = UserInfoSerializer(games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_game_by_id(request, id):
    user = UserInfo.objects.filter(id=id).first()
    if not user:
        return Response({"message": "Game Not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserInfoSerializer(user)
    return Response(serializer.data)


@api_view(["PUT"])
def update_game(request, id):
    user = UserInfo.objects.filter(id=id).first()
    if not user:
        return Response({"message": "Game Not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserInfoSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_game(request, id):
    user = UserInfo.objects.filter(id=id).first()
    if not user:
        return Response({"message": "Game Not found"}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({"message": "deleted!"}, status=status.HTTP_200_OK)