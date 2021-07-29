from rest_framework import generics
from users.models import CustomerUser
from .serializers import CustomerUserSerializer


class UserDetail(generics.RetrieveAPIView):
    serializer_class = CustomerUserSerializer
    queryset = CustomerUser.objects.all()

    def get(self, request):
        customerUserObj = queryset.objects.filter(user_id=request.user.id)
        serializer = self.get_serializer(customerUserObj)
        return Response(serializer.data)
