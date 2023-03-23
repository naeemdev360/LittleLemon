from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from .models import Booking,Menu
from .serializers import bookingSerializer,menuSerializer

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class BookingView(APIView):
     def get(self,request):
          items = Booking.objects.all()
          serializer = bookingSerializer(items,many=True)
          return Response(serializer.data)
     
     def post(self,request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        return Response({"status":"fail","message":"somethign went wrong","error":serializer.errors})
        
class MenuView(APIView):
    def get(self,request):
        items = Menu.objects.all()
        serializer = menuSerializer(items,many=True)
        return Response(serializer.data)
     
    def post(self,request):
        serializer = menuSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})

        return Response({"status":"fail","message":"somethign went wrong","error":serializer.errors})
          
          
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})       

def sayHello(request):
    return HttpResponse("Hellow world")

def index(request):
     return render(request, 'index.html', {})