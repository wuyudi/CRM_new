from django.shortcuts import render
from django.http import HttpRequest
from typing import List, Dict, Set, Tuple
from heapq import nsmallest

# 通过request.REQUEST.getlist取到list形式的提交结果
花名: List[
    str
] = "梅花、牡丹、海棠、玉兰、紫荆、连翘、金钟、丁香、紫藤、春鹃杜鹃花、石榴花、含笑花、白兰花、茉莉花、栀子花桂花、茉莉花、木芙蓉腊梅、免牙红、银芽柳、山茶花、迎春、春兰、香堇、慈菇花、风信子、郁金香、紫罗兰、金鱼草、长春菊、瓜叶菊、香豌豆夏兰、石竹、石蒜、荷花、翠菊、睡莲、芍药、福禄考、晚香玉、万寿菊、千日红建兰、铃兰报岁兰、慈茹花、香堇、大岩桐、水仙、小草兰、瓜叶菊、蒲包花、免子花、入腊红".split(
    "、"
)
鲜花图片列表: List[str] = [f"https://img.ivsky.com/img/tupian/t/202005/11/yujinxiang-0{i}.jpg" for i in range(10, 50)]
info_list: Dict[str, Tuple[str, str]] = {str(i): (j, k) for i, j, k in zip(range(10000), 花名, 鲜花图片列表)}


def recommend(shopping: List[str]) -> Set[str]:
    """推荐算法 k 近邻"""
    k = set(map(str, nsmallest(n=5, iterable=range(30), key=lambda x: sum(abs(x - int(i)) for i in shopping))))
    if k == set(shopping):
        return {"0"}
    else:
        return k - set(shopping)


def shopping_view(request: HttpRequest) -> HttpRequest:
    check_box_list: list = request.POST.getlist("check_box_list")
    recommend_: Set[str] = recommend(check_box_list)
    items: List[str] = list(map(str, range(30)))
    intro: List[Tuple[str, str]] = [info_list[i] for i in items]
    商品列表: List[Tuple[str, Tuple[str, str]]] = list(zip(items, intro))
    推荐列表 = zip(recommend_, [info_list[i] for i in recommend_], [鲜花图片列表[int(i)] for i in recommend_])
    context = {"chosen": check_box_list, "商品列表": 商品列表, "推荐列表": 推荐列表, "intro": intro}
    return render(request, "shopping.html", context=context)
