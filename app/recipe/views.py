from core.models import Recipes
from recipe import serilizers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RecipeViewSet(viewsets.ModelViewSet):
    """ View for manage recipe APIs.  """
    serializer_class = serilizers.RecipeSerializer
    queryset = Recipes.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Retrieve recipes for authenticated user. """
        return self.queryset.filter(user=self.request.user).order_by('-id')
