from cgitb import html
from itertools import count
import re
from django.shortcuts import render
from django.shortcuts import render, redirect  
from CricketLiveScores.forms import PlayerForm  
from CricketLiveScores.models import Player, Team
 
def player(request):  
    if request.method == "POST":  
        form = PlayerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form =  PlayerForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    players = Player.objects.all()  
    return render(request,"show.html",{'players':players})  

'''def edit(request, id):  
    player = Player.objects.get(pid=id)  
    return render(request,'edit.html', {'player':player})  '''
    
def update(request, id):  
    player = Player.objects.get(pid=id)  
    form = PlayerForm(instance = player)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()     
            return redirect("/show")  
    return render(request, 'edit.html', {'form': form})  
    
def destroy(request, id):  
    player = Player.objects.get(pid=id)  
    player.delete()  
    return redirect("/show")


def playgame(request):
    if request.method=='POST':
        t1=request.POST['Tn1']
        t2=request.POST['Tn2']
        overs=request.POST['overs']
        team=request.POST['team']
        t=Player.objects.filter(tid_id=t1)
        t3=Player.objects.filter(tid_id=t2)
        x=Team.objects.get(tid=t1)
        x.overs=overs
        x.Wickets=0
        x.extras=0
        x.save()
        x1=Team.objects.get(tid=t2)
        x1.overs=overs
        x1.Wickets=0
        x1.extras=0
        x1.save()
        if team!=t1:
            team1=t1
        else:
            team1=t2
        return render(request,'scores.html',{'t1':t,'t2':t3,'team':team,'team1':team1})
    return redirect("show")
global ts
global w
def scores(request):
    team=1
    team1=2
    t=Player.objects.filter(tid_id=team)
    print(len(t))
    x2=Team.objects.get(tid=team1)
    x1=Team.objects.get(tid=team)
    x=Team.objects.get(tid=team)
    overs=x.overs
    balls=0
    balls=overs*6
    count=2
    if balls>0:
        if 'one' in request.POST:
            ts+=1
        elif 'two' in request.POST:
            ts+=2
        elif 'three' in request.POST:
            ts+=3
        elif 'four' in request.POST:
            ts+=4
        elif 'six' in request.POST:
            ts+=6
        elif 'wide' in request.POST:
            ts+=1
            balls+=1
        elif 'noball' in request.POST:
            ts+=1
            balls+=1
        elif 'out' in request.POST:
            w+=1
            x.Wickets=w
            x.save()
            if w==len(t)-1:
                balls=1
        x.Score=ts
        print(ts)
        x.save()
        balls-=1
        if balls==0:
            count-=1
            if count!=0:
                x=Team.objects.filter(tid=team1)
                balls=overs*6
            else:
                print("Game Over")
                if x2.Score>x1.Score:
                    print(x2.tid)
                else:
                    print(x1.tid)
    return render(request,'play.html',{'scores':ts})
    #return redirect("show")
