from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from system_users_app.models import User
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404

###################################
# GET POSTS
###################################
@api_view(['GET'])
def get_posts(request):
    try:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({
            'statusCode': 200,
            'message': 'Get all posts query was successful',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get all posts query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# CREATE POST
###################################
@api_view(['POST'])
def create_post(request):
    try:
        # Get request body data but complex data
        data = request.data
        # Create data structure according to python
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'statusCode': 201,
                'message': 'Create post query was successful',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'statusCode': 400,
                'message': 'Create post query was failed',
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Create post query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# GET POST
###################################
@api_view(["GET"])
def get_post(request, pk):
    try:
        if request.method == 'GET':
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response({
                'statusCode': 200,
                'message': 'Get post query was successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Get post query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Get post query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# DELETE POST
###################################
@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        if request.method == 'DELETE':
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({
                'statusCode': 200,
                'message': 'Delete post query was successful',
                'deleted': True
            });
    except Post.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Delete post query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Delete post query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# UPDATE POST
###################################
@api_view(['PUT'])
def update_post(request, pk):
    try:
        data = request.data

        if request.method == 'PUT':
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'statusCode': 200,
                    'message': 'Update post query was successful',
                    'data': serializer.data
                });
            else:
                return Response({
                    'statusCode': 400,
                    'message': 'Update post query was failed',
                    'error': serializer.errors
                })
    except Post.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Update post query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Update post query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# GET POSTS BY USERID
###################################
@api_view(['GET'])
def get_posts_by_userId(request, userId):
    try:
        user = get_object_or_404(User, pk=userId)
        if(user):
            posts = Post.objects.filter(user=user)
            serializer = PostSerializer(posts, many=True)
            return Response({
                'statusCode': 200,
                'message': 'Get all posts by userId query was successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'statusCode': 403,
                'message': 'Get all posts by userId query was failed. User id not found'
            }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get all posts by userId query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)