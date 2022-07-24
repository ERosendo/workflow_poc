from rest_framework import mixins, viewsets

from .serializers import TransitionSerializer

from transition.models import Transition


class TransitionViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    
    serializer_class = TransitionSerializer
    lookup_url_kwarg = 'transition_pk'
    
    def create(self, request, *args, **kwargs):
        """
        Create transition between two states 
        """
        return super(TransitionViewSet, self).create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        """
        Destroy transition between two states 
        """
        return super(TransitionViewSet, self).destroy(request, *args, **kwargs)
    
    def get_queryset(self):
        return Transition.objects.all()
        

transition = TransitionViewSet.as_view({
    'post' : 'create'
})

transition_detail =  TransitionViewSet.as_view({
    'delete' : 'destroy'
})