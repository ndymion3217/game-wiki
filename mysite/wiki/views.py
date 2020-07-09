from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Page
from .forms import PageEditForm
import datetime

# Create your views here.
def pageView(request, page_name):  # request를 제외한 파라미터는 url을 통해 받아온다
    '''
    try:
        page_data = get_object_or_404(Page, page_name=page_name)
        content = page_data.content
        pub_date = page_data.pub_date
        context = {'page_name':page_name, 'content':content, 'pub_date':pub_date}
        return render(request, 'view.html', context)  # 파라미터로 request, html, 딕셔너리를 넣는다
    except Exception as e:
        print(e)
        context = {'page_name': page_name}  # 페이지 이름만 할당하여
        return render(request, 'create.html', context)  # 생성 페이지를 반환
    '''
    print("pageview")
    try:
        page_data = Page.objects.get(page_name=page_name)  # 파라미터로 받아온 키를 이용해 찾아서 할당
        content = page_data.content  # 위 객체의 컨텐츠를 추출
        pub_date = page_data.pub_date  # 발행일을 추출
        context = {'page_name':page_name, 'content':content, 'pub_date':pub_date}  # 템플릿에 넘길 딕셔너리제작
        return render(request, 'view.html', context)  # 파라미터로 request, html, 딕셔너리를 넣는다
    except Page.DoesNotExist:  # 혹시 없을경우
        context = {'page_name':page_name}  # 페이지 이름만 할당하여
        return render(request, 'create.html', context)  # 생성 페이지를 반환


def editView(request, page_name):  # 역시 request와 url을 받아옵니다
    try:
        page_data = Page.objects.get(page_name=page_name)
        data = {}
        data['content'] = page_data.content
        form = PageEditForm(data)
    except Page.DoesNotExist:
        form = PageEditForm()

    context = {'form': form, 'page_name': page_name}
    return render(request, 'edit.html', context)

def saveView(request, page_name):
    if request.method == 'POST':

        try:
            page_data = Page.objects.get(page_name=page_name)
            print("try")
        except Page.DoesNotExist:
            page_data = Page(page_name=page_name, content='', pub_date=datetime.datetime.now())
            print(page_data.page_name)
        form = PageEditForm(request.POST, instance=page_data)
        if form.is_valid():
            form.save()
            print("saved")

        try:
            form.save()

        except Exception as e:
            print(e)
        '''
        form = PageEditForm(request.POST)
        print(request.POST)
        print(form)
        if form.is_valid():
            print("valid!")
            post = form.save(commit=False)
            post.page_name = page_name
            post.pub_date = datetime.datetime.now()
            post.save()
        '''
        #con = sqlite3.connect("c:/Users/SDM/Documents/Github/game-wiki/mysite/db.sqlite3")
        #cur = con.cursor()
        #print(cur.fetchall())
        return HttpResponseRedirect("/wiki/" + page_name + "/")
    else:
        return HttpResponseRedirect("/wiki/" + page_name + "/edit/")