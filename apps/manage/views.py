from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """
    总览
    :param request:
    :return:
    """
    return render(request, 'overview.html', {'active_nav': 'overview'})


@login_required
def doc_view(request):
    """
    文档
    :param request:
    :return:
    """
    return render(request, 'doc/index.html', {'active_nav': 'doc'})


@login_required
def user_manage_view(request):
    """
    用户管理
    :param request:
    :return:
    """
    return render(request, 'user_and_permission/user_manage.html', {'active_nav': 'user_manage'})


@login_required
def role_manage_view(request):
    """
    角色管理
    :param request:
    :return:
    """
    return render(request, 'user_and_permission/role_manage.html', {'active_nav': 'role_manage'})


@login_required
def dept_manage_view(request):
    """
    部门管理
    :param request:
    :return:
    """
    return render(request, 'user_and_permission/dept_manage.html', {'active_nav': 'dept_manage'})


@login_required
def app_token_manage_view(request):
    """
    应用调用权限管理
    :param request:
    :return:
    """
    return render(request, 'user_and_permission/token_manage.html', {'active_nav': 'token_manage'})


@login_required
def workflow_manage_view(request):
    """
    工作流管理
    :param request:
    :return:
    """
    return render(request, 'workflow/workflow_manage.html', {'active_nav': 'workflow_manage'})


@login_required
def run_script_manage_view(request):
    """
    执行脚本管理
    :param request:
    :return:
    """
    return render(request, 'workflow/run_script_manage.html', {'active_nav': 'run_script_manage'})


@login_required
def notice_manage_view(request):
    """
    通知管理
    :param request:
    :return:
    """
    return render(request, 'workflow/notice_manage.html', {'active_nav': 'notice_manage'})


@login_required
def workflow_flow_chart_view(request, workflow_id):
    """
    工作流流程图
    :param request:
    :return:
    """
    return render(request, 'workflow/flow_chart.html', {'active_nav': 'workflow_manage', 'workflow_id':workflow_id})