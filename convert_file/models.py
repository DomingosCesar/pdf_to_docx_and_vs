from django.db import models

class ConvertedFiles(models.Model):
    input_file = models.FileField(upload_to='pdf_files/', max_length=300)
    input_path = models.FilePathField(null=True)
    output_file = models.FileField(null=True, upload_to='docx_files/', max_length=300)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
