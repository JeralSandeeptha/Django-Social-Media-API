from django.shortcuts import render
from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

###################################
# GET USERS
###################################
@api_view(['GET'])
def get_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            'statusCode': 200,
            'message': 'Get all users query was successful',
            'admins': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get all users query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# CREATE USER
###################################
@api_view(['POST'])
def create_user(request):
    try:
        # Get request body data but complex data
        data = request.data
        # Create data structure according to python
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'statusCode': 201,
                'message': 'Create user query was successful',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'statusCode': 400,
                'message': 'Create user query was failed',
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Create user query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# GET USER
###################################
@api_view(["GET"])
def get_user(request, pk):
    try:
        if request.method == 'GET':
            admin = User.objects.get(pk=pk)
            serializer = UserSerializer(admin)
            return Response({
                'statusCode': 200,
                'message': 'Get user query was successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Get user query was failed. No user was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Get user query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# UPDATE USER
###################################
@api_view(['PUT'])
def update_user(request, pk):
    try:
        data = request.data

        if request.method == 'PUT':
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'statusCode': 200,
                    'message': 'Update user query was successful',
                    'data': serializer.data
                });
            else:
                return Response({
                    'statusCode': 400,
                    'message': 'Update user query was failed',
                    'error': serializer.errors
                })
    except User.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Update user query was failed. No user was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Update user query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# DELETE USER
###################################
@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        if request.method == 'DELETE':
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({
                'statusCode': 200,
                'message': 'Delete user query was successful',
                'deleted': True
            });
    except User.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Delete user query was failed. No user was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Delete user query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)