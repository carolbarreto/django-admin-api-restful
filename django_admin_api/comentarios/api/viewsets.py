from rest_framework.viewsets import ModelViewSet
from .serializers import ComentarioSerializer
from comentarios.models import Comentarios

class ComentarioViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
    