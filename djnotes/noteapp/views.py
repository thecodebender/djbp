# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView,\
    DeleteView, DetailView
from django.core.urlresolvers import reverse
from models import Note


class NoteView(DetailView):

    model = Note
    template_name = 'note.html'


class DeleteNoteView(DeleteView):

    model = Note
    template_name = 'delete_note.html'

    def get_success_url(self):
        return reverse('notes-list')


class NoteMixin(object):

    model = Note
    template_name = 'edit_note.html'

    def get_success_url(self):
        return reverse('notes-list')

    def get_context_data(self, **kwargs):
        context = super(NoteMixin, self).get_context_data(**kwargs)
        context['action'] = self.get_action()
        return context


class UpdateNoteView(NoteMixin, UpdateView):
    def get_action(self):
        return reverse('notes-edit', kwargs={'pk': self.get_object().id})


class CreateNoteView(NoteMixin, CreateView):
    def get_action(self):
        return reverse('notes-create')

'''
class CreateNoteView(CreateView):

    model = Note
    template_name = 'edit_note.html'

    def get_success_url(self):
        return reverse('notes-list')

    def get_context_data(self, **kwargs):

        context = super(CreateNoteView, self).get_context_data(**kwargs)
        context['action'] = reverse('notes-create')
        return context


class UpdateNoteView(UpdateView):

    model = Note
    template_name = 'edit_note.html'

    def get_success_url(self):
        return reverse('notes-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateNoteView, self).get_context_data(**kwargs)
        context['action'] = reverse('notes-edit',
                                    kwargs={'pk': self.get_object().id})
        return context
'''


class ListNoteView(ListView):

    model = Note
    template_name = 'note_list.html'
