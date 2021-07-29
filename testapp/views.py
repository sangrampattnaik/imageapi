from rest_framework import generics, parsers

from .models import Image, ImageSerializer



class ImageAPIView(generics.ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
