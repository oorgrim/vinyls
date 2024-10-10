from django.views.generic import CreateView, ListView, DetailView
from vinyls.models import VinylRecord, AudioFile, Tag
from vinyls.forms import CreateUpdateVinylForm, CreateUpdateTagForm
from django.shortcuts import redirect


class CreateTagView(CreateView):
    model = Tag
    form_class = CreateUpdateTagForm
    success_url = "/vinyls/tags/"

class CreateVinylView(CreateView):
    model = VinylRecord
    form_class = CreateUpdateVinylForm
    success_url = "/vinyls/"
    def form_valid(self, form):
        vinyl_record = form.save()
        files = self.request.FILES.getlist('audio_files')
        for f in files:
            AudioFile.objects.create(vinyl_record=vinyl_record, audio_file=f)
        return redirect('vinyls:vinyl_detail', pk=vinyl_record.pk)