from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import CommentSerializer
from .models import Comment
from django.shortcuts import get_object_or_404
from posts_app.models import Post

###################################
# GET COMMENTS
###################################
@api_view(['GET'])
def get_comments(request):
    try:
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response({
            'statusCode': 200,
            'message': 'Get all comments query was successful',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get all comments query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# CREATE COMMENT
###################################
@api_view(['POST'])
def create_comment(request):
    try:
        # Get request body data but complex data
        data = request.data
        # Create data structure according to python
        serializer = CommentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'statusCode': 201,
                'message': 'Create comment query was successful',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'statusCode': 400,
                'message': 'Create comment query was failed',
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Create comment query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# GET COMMENT
###################################
@api_view(["GET"])
def get_comment(request, pk):
    try:
        if request.method == 'GET':
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response({
                'statusCode': 200,
                'message': 'Get comment query was successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Get comment query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({
            'statusCode': 500,
            'message': 'Get comment query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# DELETE COMMENT
###################################
@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        if request.method == 'DELETE':
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({
                'statusCode': 200,
                'message': 'Delete comment query was successful',
                'deleted': True
            })
    except Comment.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Delete comment query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Delete comment query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# UPDATE COMMENT
###################################
@api_view(['PUT'])
def update_comment(request, pk):
    try:
        data = request.data

        if request.method == 'PUT':
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'statusCode': 200,
                    'message': 'Update comment query was successful',
                    'data': serializer.data
                })
            else:
                return Response({
                    'statusCode': 400,
                    'message': 'Update comment query was failed',
                    'error': serializer.errors
                })
    except Comment.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Update comment query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Update comment query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

###################################
# GET COMMENTS BY POSTID
###################################
@api_view(['GET'])
def get_comments_by_postId(request, postId):
    try:
        post = get_object_or_404(Post, pk=postId)
        if(post):
            comments = Comment.objects.filter(post=post)
            # In here we can customize the object type of all posts
            comments_data = [{'commentId': comment.commentId, 'comment': comment.comment, 'username': comment.user.username, 'created_at': comment.createdAt, 'updated_at': comment.updatedAt} for comment in
                          comments]
            return Response({
                'statusCode': 200,
                'message': 'Get all comments by postId query was successful',
                'data': comments_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'statusCode': 403,
                'message': 'Get all comments by postId query was failed. User id not found'
            }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get all comments by postId query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)