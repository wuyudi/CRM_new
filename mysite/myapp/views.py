from django.shortcuts import render
from django.http import HttpRequest
from typing import List, Dict, Set

# 通过request.REQUEST.getlist取到list形式的提交结果
花名: List[
    str
] = "梅花、桃bai、牡丹、海棠、玉兰、du木笔、紫荆、连翘、金钟、丁香、紫藤、春鹃杜鹃花、石榴花、含笑花、白兰花、茉莉花、栀子花桂花、茉莉花、木芙蓉腊梅、免牙红、银芽柳、山茶花、迎春...... 常用草本花卉春兰、香堇、慈菇花、风信子、郁金香、紫罗兰、金鱼草、长春菊、瓜叶菊、香豌豆夏兰、石竹、石蒜、荷花、翠菊、睡莲、芍药、福禄考、晚香玉、万寿菊、千日红建兰、铃兰报岁兰、慈茹花、香堇、大岩桐、水仙、小草兰、瓜叶菊、蒲包花、免子花、入腊红".split(
    "、"
)
info_list: Dict[str, str] = {str(i): j for i, j in zip(range(10000), 花名)}


def recommend(shopping: List[str]) -> Set[str]:
    """推荐算法"""
    recommend_list: Dict[str, str] = {"0": "2", "1": "2", "2": "1", "3": "4", "5": "6", "6": "5", "4": "3"}
    if (k := {recommend_list[i] for i in shopping} - set(shopping)) == set():
        return {"0"}
    else:
        return k


def shopping_view(request: HttpRequest) -> HttpRequest:
    check_box_list: list = request.POST.getlist("check_box_list")
    recommend_: Set[str] = recommend(check_box_list)
    items: List[str] = ["0", "1", "2", "3", "4", "5", "6"]
    intro: List[str] = [info_list[i] for i in items]
    商品列表 = zip(items, intro)
    推荐列表 = zip(recommend_, [info_list[i] for i in recommend_])
    context = {"chosen": check_box_list, "商品列表": 商品列表, "推荐列表": 推荐列表, "intro": intro}
    return render(request, "shopping.html", context=context)
