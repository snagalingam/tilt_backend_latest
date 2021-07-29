from .serializers import UserSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create':
            permission_classes = [IsAdminUser]

        elif self.action == 'retrieve':
            permission_classes = [IsLoggedInUserOrAdmin]

        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]
