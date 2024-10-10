from django import forms
from .models import VinylRecord, AudioFile, Tag
from .widgets import MultipleFileInput

class VinylRecordForm(forms.ModelForm):
    class Meta:
        model = VinylRecord
        fields = ["title", "artist", "price", "tags", "release_date"]
        widgets = {"release_date": forms.DateInput(attrs={"type": "date"})}

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ["audio_file", "title"]

class CreateUpdateVinylForm(forms.ModelForm):
    class Meta:
        model = VinylRecord
        fields = ["title", "artist", "price", "tags", "release_date"]