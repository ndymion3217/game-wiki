from django.shortcuts import render
from django.http import Http404
from wiki.models import Page

# Create your views here.
def pageView(request, page_name):  # request를 제외한 파라미터는 url을 통해 받아온다
    content =''
    pub_date = 0
    try:
        page_data = Page.objects.get(page_name=page_name)  # 파라미터로 받아온 키를 이용해 찾아서 할당
        content = page_data.content  # 위 객체의 컨텐츠를 추출
        pub_date = page_data.pub_date  # 발행일을 추출
        context = {'page_name':page_name, 'content':content, 'pub_date':pub_date}  # 템플릿에 넘길 딕셔너리제작
        return render(request, 'view.html', context)  # 파라미터로 request, html, 딕셔너리를 넣는다
    except Page.DoesNotExist:  # 혹시 없을경우
        context = {'page_name':page_name}
        return render(request, 'create.html', context)
