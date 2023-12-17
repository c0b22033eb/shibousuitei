from django.shortcuts import render

# Create your views here.
from .forms import AgeForm
from django.http import JsonResponse
import random



def index(request):
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            #フォームから受け取ったデータを変数に格納
            if form.cleaned_data['age']:
                age = form.cleaned_data['age']
                user_age = age
                age = 100 - age
                if age < 80:
                    age = 80 + random.randint(0,20)          
            month = random.randint(1,12)
            day = random.randint(1,30)
            hour = random.randint(1,24)
            minute = random.randint(1,60)
            second = random.randint(1,60)
            death_time = f"{age}歳{month}月{day}日{hour}時{minute}分{second}秒"

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                # Ajaxリクエストの場合はJSONレスポンスを返す   
                change_age = age
                print(change_age)
                return JsonResponse({"death_time": death_time, "user_age": user_age, "change_age": change_age})
            form = AgeForm()

    else:
        form = AgeForm()
        death_time = f"XX歳XX月XX日XX時XX分XX秒"
    return render(request, 'index.html', {"death_time":death_time, 'form': form})

def select(request):
    form = request.POST
    print(form)
    age = int(form['change_age'])
    user_age = int(form['user_age'])
    select = form['select']
    if int(form['num']) == 0:
        if select == "男性":
            age *= 1.0
        elif select == "女性":
            age *= 1.05
        elif select == "その他":
            age *= 1.025
    elif int(form['num']) == 1:
        if select == "学生":
            age *= 1.1
        elif select == "会社員":
            age *= 1.0
        elif select == "公務員":
            age *= 1.1
        elif select == "自営業":
            age *= 0.95
        elif select == "主婦":
            age *= 1.05
        elif select == "その他":
            age *= 1.0
    elif int(form['num']) == 2:
        if select == "200万円未満":
            age *= 0.9
        elif select == "200万円以上400万円未満":
            age *= 0.95
        elif select == "400万円以上600万円未満":
            age *= 1.0
        elif select == "600万円以上800万円未満":
            age *= 1.05
        elif select == "800万円以上1000万円未満":
            age *= 1.1
        elif select == "1000万円以上":
            age *= 1.15
    elif int(form['num']) == 3:
        if select == "北海道":
            age *= 0.95
        elif select == "東北":
            age *= 0.95
        elif select == "関東":
            age *= 1.05
        elif select == "中部":
            age *= 1.05
        elif select == "近畿":
            age *= 1.0
        elif select == "中国":
            age *= 1.0
        elif select == "四国":
            age *= 1.0
        elif select == "九州":
            age *= 1.0
        elif select == "沖縄":
            age *= 1.0
    elif int(form['num']) == 4:
        if select == "とても良い":
            age *= 1.05
        elif select == "良い":
            age *= 1.025
        elif select == "普通":
            age *= 1.0
        elif select == "悪い":
            age *= 0.95
        elif select == "とても悪い":
            age *= 0.9
    elif int(form['num']) == 5:
        if select == "140cm未満":
            age *= 1.025
        elif select == "140cm以上150cm未満":
            age *= 1.05
        elif select == "150cm以上160cm未満":
            age *= 1.025
        elif select == "160cm以上170cm未満":
            age *= 1.0
        elif select == "170cm以上180cm未満":
            age *= 1.0
        elif select == "180cm以上190cm未満":
            age *= 0.95
        elif select == "190cm以上200cm未満":
            age *= 0.95
        elif select == "200cm以上":
            age *= 0.9
    elif int(form['num']) == 6:
        if select == "40kg未満":
            age *= 0.85
        elif select == "40kg以上50kg未満":
            age *= 0.9
        elif select == "50kg以上60kg未満":
            age *= 0.95
        elif select == "60kg以上70kg未満":
            age *= 1.0
        elif select == "70kg以上80kg未満":
            age *= 1.0
        elif select == "80kg以上90kg未満":
            age *= 0.95
        elif select == "90kg以上100kg未満":
            age *= 0.9
        elif select == "100kg以上":
            age *= 0.85
    elif int(form['num']) == 7:
        if select == "かなり吸う":
            age *= 0.85
        elif select == "吸う":
            age *= 0.9
        elif select == "ほとんど吸わない":
            age *= 1.0
        elif select == "吸わない":
            age *= 1.05
    elif int(form['num']) == 8:
        if select == "かなり飲む":
            age *= 0.9
        elif select == "飲む":
            age *= 0.95
        elif select == "ほとんど飲まない":
            age *= 1.0
        elif select == "飲まない":
            age *= 1.05
    elif int(form['num']) == 9:
        if select == "かなりする":
            age *= 1.1
        elif select == "する":
            age *= 1.1
        elif select == "ほとんどしない":
            age *= 1.0
        elif select == "しない":
            age *= 0.95
    elif int(form['num']) == 10:
        if select == "4時間未満":
            age *= 0.85
        elif select == "4時間以上6時間未満":
            age *= 0.9
        elif select == "6時間以上8時間未満":
            age *= 1.0
        elif select == "8時間以上10時間未満":
            age *= 1.0
        elif select == "10時間以上":
            age *= 0.95
    elif int(form['num']) == 11:
        if select == "はい":
            age *= 0.9
        elif select == "いいえ":
            age *= 1.0
    month = random.randint(1,12)
    day = random.randint(1,30)
    hour = random.randint(1,24)
    minute = random.randint(1,60)
    second = random.randint(1,60)
    age = int(age)
    death_time = f"{age}歳{month}月{day}日{hour}時{minute}分{second}秒"
    comment = ""
    # 最初に入力された年齢と最終的に割り出された死亡年齢によってコメントを複雑に変える
    if user_age <= 20:
        if age < user_age:
            comment = "あなたは既に死んでいます　成仏してください"
        elif abs(user_age - age) <= 10:
            comment = "ざんねん　あなたは若くして死にました"
        elif 10 < abs(user_age - age) <= 20:
            comment = "あ～　中途半端な人生でしたね"
        elif 20 < abs(user_age - age) <= 40:
            comment = "お～　上々な人生でしたね！"
        elif 40 < abs(user_age - age) <= 60:
            comment = "おめでとう　人並みに長生きしました"
        else:
            comment = "おつかれさま　あなたは長生きしました"
    elif user_age <= 40:
        if age < user_age:
            comment = "あなたは既に死んでいます　成仏してください"
        elif abs(user_age - age) <= 10:
            comment = "いくらでも改善の余地はありました..."
        elif 10 < abs(user_age - age) <= 20:
            comment = "くやしそうでしたが..."
        elif 20 < abs(user_age - age) <= 40:
            comment = "おめでとう　人並みに長生きしました"
        else:
            comment = "おつかれさま　あなたは長生きしました"
    elif user_age <= 60:
        if age < user_age:
            comment = "あなたは既に死んでいます　成仏してください"
        elif abs(user_age - age) <= 10:
            comment = "趣味を謳歌してましたね"
        elif 10 < abs(user_age - age) <= 20:
            comment = "いい笑顔でしたね"
        else:
            comment = "おつかれさま　あなたは長生きしました"
    elif user_age <= 80:
        if age < user_age:
            comment = "あなたは既に死んでいます　成仏してください"
        else:
            comment = "おつかれさま　あなたは長生きしました"
    else:
        if age < user_age:
            comment = "あなたは既に死んでいます　成仏してください"
        else:
            comment = "おつかれさま　あなたは長生きしました"
    return JsonResponse({"death_time": death_time, "age": age, "comment": comment})


