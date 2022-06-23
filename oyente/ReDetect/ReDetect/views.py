import glob
import json
import os

from django.http import HttpResponse

from django.shortcuts import render

# def runoob(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'runoob.html', context)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATICFILES_DIRS = os.path.join(BASE_DIR, "upload")


def redetect(req):
    # print("前端数据: ", req.POST)
    # print("file:", req.FILES)
    #
    # for item in req.FILES:
    #     obj = req.FILES.get(item)  # 获取要写入的文件
    #     filename = obj.name  # 获取文件名
    #     f = open(os.path.join(STATICFILES_DIRS, filename), 'wb')
    #     for line in obj.chunks():  # 分块写入
    #         f.write(line)
    #     f.close()
    context = {}
    context['result'] = ''
    return render(req, "index.html", context)


def solidity(req):
    print("前端数据: ", req.POST)
    print("file:", req.FILES)
    context = {}
    context['result'] = ''
    for item in req.FILES:
        obj = req.FILES.get(item)  # 获取要写入的文件
        filename = obj.name  # 获取文件名
        f = open(os.path.join(STATICFILES_DIRS, filename), 'wb')
        for line in obj.chunks():  # 分块写入
            f.write(line)
        f.close()
        os.system('python3 /home/richael/oyente-master/oyente/oyente.py -ll 200 -s ' + os.path.join(STATICFILES_DIRS, filename) + ' -j')

        files = glob.glob(os.path.join(STATICFILES_DIRS, filename) + "*.json")
        for file in files:
            tmp = json.loads(open(file).read())
            if len(tmp['vulnerabilities']['reentrancy']) != 0:
                for s in tmp['vulnerabilities']['reentrancy']:
                    context['result'] = context['result'] + '\n' + s
            if len(tmp['vulnerabilities']['gas_hardcoded']) != 0:
                for s in tmp['vulnerabilities']['gas_hardcoded']:
                    context['result'] = context['result'] + '\n' + s
            if len(tmp['vulnerabilities']['unexpected_ether']) != 0:
                for s in tmp['vulnerabilities']['unexpected_ether']:
                    context['result'] = context['result'] + '\n' + s

    return render(req, "index.html", context)


def evm(req):
    print("前端数据: ", req.POST)
    print("file:", req.FILES)
    context = {}
    context['result'] = ''
    for item in req.FILES:
        obj = req.FILES.get(item)  # 获取要写入的文件
        filename = obj.name  # 获取文件名
        f = open(os.path.join(STATICFILES_DIRS, filename), 'wb')
        for line in obj.chunks():  # 分块写入
            f.write(line)
        f.close()
        os.system('python3 /home/richael/oyente-master/oyente/oyente.py -ll 200 -s ' + os.path.join(STATICFILES_DIRS,
                                                                                                    filename) + ' -b -j')

        files = glob.glob(os.path.join(STATICFILES_DIRS, filename) + "*.json")
        for file in files:
            tmp = json.loads(open(file).read())
            if tmp['vulnerabilities']['reentrancy']:
                context['result'] = context['result'] + '\n' + 'reentrancy:' + 'true'
            if tmp['vulnerabilities']['gas_hardcoded']:
                context['result'] = context['result'] + '\n' + 'gas_hardcoded:' + 'true'
            if tmp['vulnerabilities']['unexpected_ether']:
                context['result'] = context['result'] + '\n' + 'unexpected_ether:' + "ture"

    return render(req, "index.html", context)