from django.shortcuts import render,redirect
from iblogger24.models import Round,Post,link
from iblogger24.idx_gen import token_gen
# Create your views here.
def Home(request,link_idx):
    idx = token_gen()
    s = Round(rounds=1,rounds_idx=idx)
    s.save()
    final = Round.objects.get(rounds_idx=idx)
    link_info = link.objects.get(Link_idx=link_idx)
    post = Post.objects.get(con_number=0)
    title = post.title
    content = post.content
    final_link = f"/iblogger24/Continue/{idx}/{link_info.Link_idx}"
    step = final.rounds
    return render(request, 'templates/index.html',{'link':final_link,'title':title,'content':content,'step':step})

def roundation(request,round_idx,link_idx):
    final = Round.objects.get(rounds_idx=round_idx)
    link_info = link.objects.get(Link_idx=link_idx)
    final.rounds = final.rounds+1
    final.save()
    if final.rounds == 4:
        final_link = f"/iblogger24/Get-Link/{round_idx}/{link_info.Link_idx}"
        return redirect(final_link)
    else:
        step = final.rounds
        final_link = f"/iblogger24/Continue/{round_idx}/{link_info.Link_idx}"
        return render(request, 'templates/round.html',{'link':final_link,'step':step})
    
def get_link(request,round_idx,link_idx):
    final = Round.objects.get(rounds_idx=round_idx)
    link_info = link.objects.get(Link_idx=link_idx)
    final_link = link_info.Link
    step = final.rounds
    return render(request, 'templates/final.html',{'link':final_link,'step':step})

def download(request,round_idx,link_idx):
    link_info = link.objects.get(Link_idx=link_idx)
    final_link = link_info.Link
    return render(request, 'templates/download.html',{'link':final_link})
