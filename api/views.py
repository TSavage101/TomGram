from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth.models import User

from core.models import Profile, Follow, Post

from .serializers import ProfileSerializer

# Create your api views here.
@api_view(['GET'])
def getFollowers(request, profile, *args, **kwargs):
    get_user = User.objects.get(username=profile)
    get_profile = Profile.objects.get(user=get_user, id_user=get_user.id) # type: ignore
    
    serializer = ProfileSerializer(get_profile, many=False)
    return Response(serializer.data)