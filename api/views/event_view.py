from rest_framework import generics

from api.models import Event
from api.serializers import EventSerializer


class EventViewSet(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SingleEventViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


"""
class EventViewSet(generics.GenericAPIView, mixins.CreateModelMixin):
    def create(self, request, *args, **kwargs):
        #Create and store a new event in the database
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            # Invalid data
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
"""
