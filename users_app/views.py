from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Admin
from .serializer import AdminSerializer

###################################
# GET ADMINS
###################################
@api_view(['GET'])
def getAllAdmins(request):
    try: 
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True);
        return Response({
            'statusCode': 200,
            'message': 'Get all admins query was successful',
            'admins': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get all admins query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# CREATE ADMIN
###################################
@api_view(['POST'])
def createAdmin(request):
    try:
        # Get request body data but complex data
        data = request.data;
        # Create data structure according to python
        serializer = AdminSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'statusCode': 201,
                'message': 'Create admin query was successful',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'statusCode': 400,
                'message': 'Create admin query was failed',
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Create admin query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
###################################
# GET ADMIN
###################################
@api_view(["GET"])
def getAdmin(request, pk):
    try:
        if request.method == 'GET':
            admin = Admin.objects.get(pk=pk)
            serializer = AdminSerializer(admin)
            return Response({
                'statusCode': 200,
                'message': 'Get admin query was successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
    except Admin.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Get admin query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Get admin query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
###################################
# DELETE ADMIN
###################################
@api_view(['DELETE'])
def deleteAdmin(request, pk):
    try:
        if request.method == 'DELETE':
            admin = Admin.objects.get(pk=pk)
            admin.delete();
            return Response({
                'statusCode': 200,
                'message': 'Delete admin query was successful',
                'deleted': True
            });
    except Admin.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Delete admin query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Delete admin query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
###################################
# UPDATE BOOK
###################################
@api_view(['PUT'])
def updateAdmin(request, pk):
    try:
        data = request.data;

        if request.method == 'PUT':
            admin = Admin.objects.get(pk=pk)
            serializer = AdminSerializer(admin, data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'statusCode': 200,
                    'message': 'Update admin query was successful',
                    'data': serializer.data
                });
            else:
                return Response({
                    'statusCode': 400,
                    'message': 'Update admin query was failed',
                    'error': serializer.errors
                });
    except Admin.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Update admin query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Update admin query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)