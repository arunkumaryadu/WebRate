from django.shortcuts import render
from django.http import HttpResponse


from website.form import commentForm
from website.models import Comment
from website.models import website
from django.contrib.auth.models import User
from textblob import TextBlob
from website import form

def search_all(request):
    query=request.GET.get('search_all')
    search=website.objects.filter(website_name=query)
    for i in search:
        webView(request,i.id)
        print(i.id)




def web_detail(request):
    wc1=website.objects.all()
    wc2=website.objects.filter(website_category='E-COM')
    wc3=website.objects.filter(website_category='NEWS')
    wc4=website.objects.filter(website_category='SOCIAL')

    search_all(request)
    return render(request,'website/home.html',{'wc1':wc1,'wc2':wc2,'wc3':wc3,'wc4':wc4})



def webView(request,wid):

    w2=website.objects.filter(id=wid)
    w3=Comment.objects.filter(webid=wid)

    total_polar=0
    count=0
    for i in w3:
        count=count+1
        total_polar=total_polar+i.polar
    try:
        tpolar=total_polar/count
    except:
        tpolar=0

    #print(total_polar)
    #print(tpolar)
    #print(count)
    total_rating=comment_rating(total_polar)
    #print(total_rating)

    oneStar = Comment.objects.filter(webid=wid, rating=1).count()
    twoStar = Comment.objects.filter(webid=wid, rating=2).count()
    threeStar = Comment.objects.filter(webid=wid, rating=3).count()
    fourStar = Comment.objects.filter(webid=wid, rating=4).count()
    fiveStar = Comment.objects.filter(webid=wid, rating=5).count()

    print("one star ",oneStar)



    my_dict={

    'w2':w2,
    'total_rating':total_rating,
    'w3':w3,'count':count,
    'oneStar':oneStar,
    'twoStar':twoStar,
    'threeStar':threeStar,
    'fourStar':fourStar,
    'fiveStar':fiveStar
    }
    return render(request,'website/webView.html',context=my_dict)

def commentview(request,uid,wid):


    w2=website.objects.filter(id=wid)
    w3=Comment.objects.filter(webid=wid)
    total_polar=0
    count=0
    for i in w3:
        count=count+1
        total_polar=total_polar+i.polar
    try:
        tpolar=total_polar/count
    except:
        tpolar=0

    #print(total_polar)
    #print(tpolar)
    #print(count)
    total_rating=comment_rating(total_polar)
    #print(total_rating)

    oneStar = Comment.objects.filter(webid=wid, rating=1).count()
    twoStar = Comment.objects.filter(webid=wid, rating=2).count()
    threeStar = Comment.objects.filter(webid=wid, rating=3).count()
    fourStar = Comment.objects.filter(webid=wid, rating=4).count()
    fiveStar = Comment.objects.filter(webid=wid, rating=5).count()

    print("one star ",oneStar)



    commentform = commentForm()
    if request.method=='POST':
        commentform=commentForm(request.POST)

        if commentform.is_valid():
            cmt=request.POST['coment']
            print(cmt)
            print(uid)
            print(wid)
            saveComment(cmt,uid,wid)
            #commentform.save(commit=True)
            return web_detail(request)
        else:
            print('Your review not save')

    my_dict={'form':commentform,
    'w2':w2,
    'total_rating':total_rating,
    'w3':w3,'count':count,
    'oneStar':oneStar,
    'twoStar':twoStar,
    'threeStar':threeStar,
    'fourStar':fourStar,
    'fiveStar':fiveStar
    }
    return render(request,'website/comment.html',context=my_dict)

def saveComment(comment,uid1,wid1):
    c=Comment()
    co=comment
    w=website.objects.get(id=wid1)
    u=User.objects.get(id=uid1)
    c.coment=comment
    c.webid=w
    c.user_id=u
    pp=polarity_comment(co)
    c.polar=pp
    c.rating=comment_rating(pp)
    c.save()

def polarity_comment(string):
    string=TextBlob(string).sentiment.polarity
    return string




def comment_rating(number):
    Range=3
    if number>=-1 and number<-0.5:
        Range=1
    elif number>=-0.5 and number<0.0:
        Range=2
    elif number is 0.0:
        Range=3
    elif number>0.0 and number<0.5:
        Range=4
    elif number>=0.5 and number<1.0:
        Range=5



    return Range

def about(request):
    return render(request, 'website/About.html')

def contact(request):
    return render(request, 'website/Contact.html')
