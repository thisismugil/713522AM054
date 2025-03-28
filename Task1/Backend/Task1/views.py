import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

BASE_URL = "http://20.244.56.144/test"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQzMTUzODcwLCJpYXQiOjE3NDMxNTM1NzAsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjAxZjZjZjhmLTYyNjMtNDM4YS1iOGRmLWRmZDkyNWE2M2I1ZSIsInN1YiI6Im11Z2lsMTIwNkBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJnb01hcnQiLCJjbGllbnRJRCI6IjAxZjZjZjhmLTYyNjMtNDM4YS1iOGRmLWRmZDkyNWE2M2I1ZSIsImNsaWVudFNlY3JldCI6ImNVRmFVVnFoREhmVVBuSEciLCJvd25lck5hbWUiOiJSYWh1bCIsIm93bmVyRW1haWwiOiJtdWdpbDEyMDZAZ21haWwuY29tIiwicm9sbE5vIjoiNzEzNTIyQU0wNTQifQ.dqTZNQG06331QFF3wEfEAa3JDSQznrqYeh-mIMU6eOI"  # Replace with actual API token

@api_view(['POST'])
def user(request):
    user_data = request.data
    serializer = UserSerializer(data=user_data)
    if serializer.is_valid():
        user_instance = serializer.save()
        try:
            response = requests.post(f"{BASE_URL}/users", json=user_data)
            if response.status_code == 200:
                return Response(response.json(), status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "saving in local"},
                    status=status.HTTP_206_PARTIAL_CONTENT
                )
        except requests.exceptions.RequestException as e:
            return Response(
                {"message": f"user saved locally{str(e)}"},
                status=status.HTTP_206_PARTIAL_CONTENT
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request):
    try:
        response = requests.get(f"{BASE_URL}/users")
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
    except requests.exceptions.RequestException:
        pass
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_posts(request, user_id):
    posts_url = f"{BASE_URL}/users/{user_id}/posts"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    try:
        response = requests.get(posts_url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data.get("posts"):
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "no posts"},
                    status=status.HTTP_204_NO_CONTENT
                )
        elif response.status_code == 401:
            return Response(
                {"error": "unauthorized"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        else:
            return Response(
                {"error": "failed api"},
                status=response.status_code
            )
    except requests.exceptions.RequestException as e:
        return Response(
            {"error": f"failed api{str(e)}"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
        
@api_view(['GET'])
def get_post_comments(request, post_id):
    comments_url = f"{BASE_URL}/posts/{post_id}/comments"
    try:
        response = requests.get(comments_url)
        
        if response.status_code == 200:
            data = response.json()
            if "comments" in data and data["comments"]:
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "no comments"},
                    status=status.HTTP_204_NO_CONTENT
                )
        else:
            return Response(
                {"error": "failed api"},
                status=response.status_code
            )
    except requests.exceptions.RequestException as e:
        return Response(
            {"error": f"failed api{str(e)}"},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
