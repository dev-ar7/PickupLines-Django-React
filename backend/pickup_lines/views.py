from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import PickupLines
from .serializer import PickupLinesSerializer
from rest_framework_word_filter import FullWordSearchFilter  # For searching by a full word(more info: https://github.com/trollknurr/django-rest-framework-word-search-filter)


class PickupLineCreateView(generics.CreateAPIView):

    queryset = PickupLines.objects.all()
    serializer_class = PickupLinesSerializer

    def post(self, request):

        if request.method == 'POST':
            line = request.data.get('line')
            line_exists= PickupLines.objects.filter(line = line).exists()
            if line_exists:
                return Response({'message': 'Line Already exists! Try with a unique one.'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Line saved to our database. We are very thankful for all the great lines that were submitted by you!'},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PickupLinesView(generics.ListAPIView):

    queryset = PickupLines.objects.all()
    serializer_class = PickupLinesSerializer
    filter_backends = [filters.SearchFilter, FullWordSearchFilter]
    search_fields = ['line', 'cat', 'tag']
    word_fields = ('text',)

