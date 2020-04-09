from django.shortcuts import render
from .models import Metadata, Document
from .serializers import MetadataSerializer, DocumentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, status, exceptions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication



class MetadataView(viewsets.ModelViewSet):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        query = super().get_queryset()

        name = self.request.query_params.get('name',None)
        if name:
            query = query.filter(name=name)
        return query



class DocumentView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        query = super().get_queryset()

        name = self.request.query_params.get('name',None)
        if name:
           query = query.filter(name=name)
        return query
    
    def create(self, request):
        request.data["x"] = ""
        return super(DocumentView, self).create(request)
