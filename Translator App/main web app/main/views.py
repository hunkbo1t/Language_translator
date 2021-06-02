from .model import *
def index(request):
    return render(request, 'home.html', {} )

def second(request):
    gt.key = request.POST['Select1']
    gt.Text = request.POST['text1']
    trans = str(trs.translate(gt.Text,lang_tgt=gt.key,lang_src='auto'))
    return render(request,'second.html',{'trans':trans})