from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect


LOGIN_REQUIRED_URLS = ['/teachers/', '/praise/',
                       '/criticize/', '/excel/', '/teachers_data/']


def check_login_middleware(get_resp):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if request.path in LOGIN_REQUIRED_URLS:
            if 'userid' not in request.session:
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'code': 10003, 'hint': '请先登录'})
                else:
                    backurl = request.get_full_path()
                    return redirect(f'/login/?backurl={backurl}')
        return get_resp(request, *args, **kwargs)
    return wrapper
