from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(
    max_length=50,
    unique=True,
    verbose_name=_("Название тега"),
    help_text=_("Введите название тега (максимум 50 символов)"),
    )
    class Meta:
        verbose_name = _("Тег")
        verbose_name_plural = _("Теги")
        ordering = ["name"]
    def __str__(self):
        return self.name

class VinylRecord(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название альбома"))
    artist = models.CharField(max_length=255, verbose_name=_("Исполнитель"))
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    tags = models.ManyToManyField(Tag, related_name="records", blank=True)
    release_date = models.DateField(null=True, blank=True)

class AudioFile(models.Model):
    vinyl_record = models.ForeignKey(VinylRecord, on_delete=models.CASCADE, related_name="audio_files")
    audio_file = models.FileField(upload_to="vinyl_audio/")
    title = models.CharField(max_length=255, blank=True)