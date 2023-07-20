from django.shortcuts import render
from . models import Notes

from django.views.generic import DetailView, ListView

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/list_notes.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/list_notes.html', {'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail_notes.html'
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#         return render(request, 'notes/detail_notes.html', {'note': note})
#     except Notes.DoesNotExist:
#         return render(request, 'notes/page_not_found.html', {})