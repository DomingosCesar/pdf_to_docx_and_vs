from django.shortcuts import render, HttpResponse, redirect
from . import convertion
from . import models

def index(request):
    # form = forms.FilesForm()
    if request.method == 'POST':
        # form = forms.FilesForm(request.POST['input_file'], request.FILES)
        # print(request.POST)
        # print(form)
        # if form.is_valid():
        
        #     print(file)
        #     done = models.ConvertedFiles(request.POST['input_file'])
        #     done.outpu_file = file
        #     done.save()
        #     return redirect('index')
        docx = request.POST['input_path']
        # file = f"{docx[:len(docx) - 3]}.docx"
        # done = models.ConvertedFiles(input_file = request.POST['input_file'], output_file = file)
        # done.save()
        # cv = convertion.Converte_to()
        # cv.converte_pdf_to_docx()
        print(docx)
        
        return HttpResponse('<h2> Feito com sucesso!</h2>')
        # else:
        #     return HttpResponse('<h2> form invalido</h2>')
    return render(request, 'convert_file/index.html')
