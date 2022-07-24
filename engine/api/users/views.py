from api.users.serializers import (CreateUserSerializer, UserSerializer,
                                      UserUpdateSerializer)
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from user.models import User


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = UserSerializer
    serializer_action_classes = {
        'partial_update': UserUpdateSerializer
    }

    lookup_url_kwarg = 'user_pk'

    def list(self, request, *args, **kwargs):
        """
        Retrieve list of users from database.
        ---
        example:
            {}
        TODO: Add docstrings for swagger
        """
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve certain user from database.
        ---
        example:
            {}
        TODO: Add docstrings for swagger
        """
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Updates an user from database.
        ---
        example:
            {}
        TODO: Add docstrings for swagger
        """
        return super(UserViewSet, self).partial_update(request, *args, **kwargs)
    
    
    def create(self, request, *args, **kwargs):
        """
        Creates a user.
        ---
        example:
            {}
        TODO: Add docstrings for swagger
        """

        serializer = CreateUserSerializer(data=request.data, context={
            'request': request,
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        qs = User.objects.all()
        return qs
    
    
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update'
})
