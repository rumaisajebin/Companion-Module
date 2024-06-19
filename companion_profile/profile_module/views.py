from rest_framework import generics, permissions
from .models import Companion_profile
from .serializers import CompanionProfileSerializer

# Create your views here.

class CompanionProfileListView(generics.ListAPIView):
    queryset = Companion_profile.objects.all()
    serializer_class = CompanionProfileSerializer
    permission_classes = [permissions.AllowAny]
    
class CompanionProfileDetailListView(generics.RetrieveAPIView):
    queryset = Companion_profile.objects.all()
    serializer_class = CompanionProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    
class CompanionProfileCreateView(generics.CreateAPIView):
    queryset = Companion_profile.objects.all()
    serializer_class = CompanionProfileSerializer
    permission_classes = [permissions.AllowAny]
    
class CompanionProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Companion_profile.objects.all()
    serializer_class = CompanionProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    
class CompanionProfileDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Companion_profile.objects.all()
    serializer_class = CompanionProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'