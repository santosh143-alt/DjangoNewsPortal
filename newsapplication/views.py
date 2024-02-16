from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'newsapplication/index.html')

def movie_view(request):
    head_msg = 'Santosh Movie News'
    m1="Meet Ishaan Khatter's girlfriend"
    m2='Deepika Padukone becomes global brand ambassador'
    m3='Priyanka Chopra shares unseen wedding pic from grand Jodhpur ceremony'
    m4='Ranveer Singh to play Shaktimaan'
    m5='Craze of bitcoin in bollywood industry'
    type='movies'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request, 'newsapplication/news.html',my_dict)

def sports_view(request):
    head_msg = 'Santosh Sports News'
    m1="Surprise win rocks basketball world"
    m2='Boxing champion defends title triumphantly'
    m3='Swimming sensation breaks pool records'
    m4='Boxing champion defends title triumphantly'
    m5='Cycling superstar conquers mountain stage'
    type='sports'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request, 'newsapplication/news.html',my_dict)

def political_view(request):
    head_msg = 'Santosh Political News'
    m1="Election turmoil grips Indian parliament"
    m2='Supreme Court delivers landmark verdict'
    m3='Ruling party faces internal leadership challenge'
    m4='Cabinet reshuffle shakes political landscape'
    m5='State elections see unexpected power shifts'
    type='politics'
    my_dict={'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request, 'newsapplication/news.html',my_dict)
