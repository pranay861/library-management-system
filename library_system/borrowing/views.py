from django.shortcuts import render, get_object_or_404
from .models import Borrowing


def borrowing_list(request):
    borrowings = Borrowing.objects.all()
    return render(request, 'borrowing/borrowing_list.html', {'borrowings': borrowings})


def borrowing_detail(request, pk):
    borrowing = get_object_or_404(Borrowing, pk=pk)
    return render(request, 'borrowing/borrowing_detail.html', {'borrowing': borrowing})
