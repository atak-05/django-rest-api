from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from comment.api.paginations import CommentPagination
from comment.api.permissions import IsOwner

#mixinsler
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from comment.api.serialiizers import CommentCreateSerializers, CommentListSerializers, CommentDeleteUpdateSerializer
from comment.models import Comment


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    pagination_class = CommentPagination

    def get_queryset(self):
        return Comment.objects.filter(parent=None)
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(post=query)
        return queryset


# class CommentDeleteAPIView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):
    # queryset = Comment.objects.all()
    # serializer_class = CommentDeleteUpdateSerializer
    # lookup_field = "pk"
    # permission_classes = [IsOwner]
    
    # def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)
    # def get (self,request, *args,  **kwargs):
        # return self.retrieve(request, *args, **kwargs)
        


class CommentUpdateAPIView(UpdateAPIView, RetrieveAPIView, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = "pk"
    permission_classes = [IsOwner]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)