from django.contrib import admin
from .models import VinylRecord, AudioFile, Tag

@admin.register(VinylRecord)
class VinylRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'price', 'release_date')

@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('vinyl_record', 'audio_file')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)