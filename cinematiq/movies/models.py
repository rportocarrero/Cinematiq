
from django.db import models

# Function to get the movie directory path
def movie_directory_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/movies/movie_<id>/<filename>
    return 'movies/movie_{0}/{1}'.format(instance.id, filename)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    hls_file_url = models.FileField(upload_to=movie_directory_path)