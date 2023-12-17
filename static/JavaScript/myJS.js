var num = 0;
var user_age = 0;
var change_age = 0;
$('#questionnaire').submit(function(event) {
    event.preventDefault(); // フォームの標準動作を防ぐ
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val(); // CSRFトークンを取得
    var userInput = $('#questionnaire input[name="age"]').val(); // ユーザー入力を取得

    $.ajax({
        type: 'POST',
        url: '/', // DjangoビューのURL
        data: {
            age: userInput,
            csrfmiddlewaretoken: csrfToken
        },
        success: function(response) {
            // サーバーからの応答をページに表示
            // $('#death-time').text(response.death_time); // サーバーから返されたdeath_timeで更新 
            user_age = response.user_age;
            change_age = response.change_age;
            $('#questionnaire').hide(); // アンケートフォームを非表示にする
            // フォーム内のテキストをクリア
            $('#questionnaire input[name="age"]').val('');

            // situmonをよびだす
            situmon(situmons, num);
        }
    });
});

var situmons = [
    {
        "situmon": "あなたの性別を教えてください",
        "sentakusi": [
            "男性",
            "女性",
            "その他"
        ]
    },
    {
        "situmon": "あなたの職業を教えてください",
        "sentakusi": [
            "学生",
            "会社員",
            "公務員",
            "自営業",
            "主婦",
            "その他"
        ]
    },
    {
        "situmon": "あなたの年収を教えてください",
        "sentakusi": [
            "200万円未満",
            "200万円以上400万円未満",
            "400万円以上600万円未満",
            "600万円以上800万円未満",
            "800万円以上1000万円未満",
            "1000万円以上"
        ]
    },
    {
        "situmon": "あなたの住んでいる地域を教えてください",
        "sentakusi": [
            "北海道",
            "東北",
            "関東",
            "中部",
            "近畿",
            "中国",
            "四国",
            "九州",
            "沖縄"
        ]
    },
    {
        "situmon": "あなたの健康状態を教えてください",
        "sentakusi": [
            "とても良い",
            "良い",
            "普通",
            "悪い",
            "とても悪い"
        ]
    },
    {
        "situmon": "あなたの身長を教えてください", 
        "sentakusi": [
            "140cm未満",
            "140cm以上150cm未満",
            "150cm以上160cm未満",
            "160cm以上170cm未満",
            "170cm以上180cm未満",
            "180cm以上190cm未満",
            "190cm以上200cm未満",
            "200cm以上"
        ]
    },
    {
        "situmon": "あなたの体重を教えてください",
        "sentakusi": [
            "40kg未満",
            "40kg以上50kg未満",
            "50kg以上60kg未満",
            "60kg以上70kg未満",
            "70kg以上80kg未満",
            "80kg以上90kg未満",
            "90kg以上100kg未満",
            "100kg以上"
        ]
    },
    {
        "situmon": "あなたの喫煙習慣を教えてください",
        "sentakusi": [
            "かなり吸う",
            "吸う",
            "ほとんど吸わない",
            "吸わない",

        ]
    },
    {
        "situmon": "あなたの飲酒習慣を教えてください",
        "sentakusi": [
            "かなり飲む",
            "飲む",
            "ほとんど飲まない",
            "飲まない",          

        ]
    },
    {
         "situmon": "あなたの運動習慣を教えてください",
        "sentakusi": [
            "かなりする",
            "する",
            "ほとんどしない",
            "しない"
        ]
    },
    {
        "situmon": "あなたの睡眠時間を教えてください",
        "sentakusi": [
            "4時間未満",
            "4時間以上6時間未満",
            "6時間以上8時間未満",
            "8時間以上10時間未満",
            "10時間以上"
        ]
    },
    {
        "situmon": "あなたは死にたいと思ったことがありますか？",
        "sentakusi": [
            "はい",
            "いいえ"
        ]
    }
]; // 質問のリスト

// 呼び出されたら質問と選択肢を表示し、選択肢をクリックしたらサーバーに選択肢を送信し、新たな質問と選択肢を表示する
function situmon(situmons, num){
    $('#number').text("質問" + (num + 1));
    //numの値にもとづいて質問を表示
    $('#question').text(situmons[num].situmon);
    // もしボタンがあれば削除
    $('#sentakusi input').remove();
    // sentakusiの要素数にもとづいてボタンと選択肢を表示または追加
    for (var i = 0; i < situmons[num].sentakusi.length; i++) {
        // ボタンを追加
        $('#sentakusi').append('<input type="submit" name="sentakusi" value="' + situmons[num].sentakusi[i] + '">' );

    }
}

$('#sentakusi').on('click', 'input[type="submit"]', function(event) {
    event.preventDefault(); // フォームの標準動作を防ぐ
    // 選択されたボタンの値を取得
    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
    var clickedButton = $(this);
    userselect = clickedButton.val(); 
    $.ajax({
        type: 'POST',
        url: 'shibousuitei/', // DjangoビューのURL
        data: {
            num: num,
            select: userselect,
            csrfmiddlewaretoken: csrfToken,
            user_age: user_age,
            change_age: change_age
        },
        success: function(response) {
            // $('#death-time').text(response.death_time); // サーバーから返されたdeath_timeで更新 
            $('#questionnaire').hide(); // アンケートフォームを非表示にする
            num += 1;
            console.log(num);
            // numが質問の数より小さい場合
            if (num < situmons.length){
                // situmonをよびだす
                situmon(situmons, num);
                change_age = response.age;
            }
            // numが質問の数以上の場合
            else{
                // 結果を表示
                $('#death-time').text(response.death_time); 
                $('#number').hide();
                $('#sentakusi').text(response.comment);
                //　質問を非表示にする
                $('#question').hide();
                
            }
        }
    });
});

