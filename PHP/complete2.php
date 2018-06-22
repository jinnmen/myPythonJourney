<?php
/* if ($_SERVER['HTTP_REFERER'] == null){
    header('Location: top.php');
    exit;
}*/
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $website = $_POST["website"];
    $comment = $_POST["comment"];
    $gender = $_POST["gender"];

    try {
    
    /*ここからPDO*/
    
        $dsn = 'mysql:dbname=Train1;host=localhost;charset=utf8';
        $user = 'root';
        $password = '';
    
        $dbh = new PDO($dsn, $user, $password);
        $dbh->query('SET NAMES utf8');
        $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, true);
        $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); /*エラーメッセージ吐いてくれる*/
    
        $sql = 'INSERT INTO `formt` (`Name`, `Email`, `Website`, `Comment`, `Gender`) VALUES (?, ?, ?, ?, ?, ?)';
        $stmt = $dbh->prepare($sql);
    
    
        $stmt->bindValue(1, $name, PDO::PARAM_STR);
        $stmt->bindValue(2, $email, PDO::PARAM_STR);
        $stmt->bindValue(3, $website, PDO::PARAM_STR);
        $stmt->bindValue(4, $comment, PDO::PARAM_STR);
        $stmt->bindValue(5, $gender, PDO::PARAM_STR);
        $stmt->bindValue(6, date("Y-m-d H:i:s"), PDO::PARAM_STR);
    
        $stmt->execute();
        $id = $dbh->lastInsertId();
    
    /*ここまでPDO*/

        mb_language("Japanese");
        mb_internal_encoding("UTF-8");

        $to_company = /*運営者アドレス*/ "jinnmen.leong@plan-b.co.jp"; 
        $to_customer = $mailText;
        $title_to_company = "お客様からのお問い合わせ内容";
        $title_to_customer = "お問い合わせ有難う御座います";

        $body_header_to_company = "お客様からのお問い合わせ情報です。\n";
        $body_header_to_customer = "この度はお問い合わせいただき有難う御座います。下記の内容でお問い合わせを受け付けました。\n";
        $body_main = <<< EOM
      
===================================================
【 お名前 】 
{$name}

【 メール 】 
{$email}

【 ウェブサイト 】 
{$website}

【 コメント 】 
{$comment}

【 性別 】 
{$gender}
===================================================
\n
EOM;

        $body_footer_to_company = "対応お願いします。";
        $body_footer_to_customer = "ご確認よろしくお願いします。";

        if(!mb_send_mail($to_company, $title_to_company, $body_header_to_company . $body_main . $body_footer_to_company)){
            echo "メールの送信に失敗しました";
            exit();
        }

        if(!mb_send_mail($to_customer, $title_to_customer, $body_header_to_customer . $body_main . $body_footer_to_customer)){
            echo "メールの送信に失敗しました";
            exit();
        };
        header('Location: complete.php');
        exit;
    
      } catch (PDOException $e) {
        echo $e->getMessage();
        exit;
      }
    }
?>


<html lang='jp'>
<head>
    <title>完了画面フォーム</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <ul class="breadcrumb">
        <li itemscope="itemscope" itemtype="http://data-vocabulary.org/Breadcrumb">
        <a href="top.php" itemprop="url">
                <span itemprop="title">TOP</span>
        </a>
        </li>
        <li itemscope="itemscope" itemtype="http://data-vocabulary.org/Breadcrumb">
                <span itemprop="title">お問合せフォーム</span>
        </li>
        <li itemscope="itemscope" itemtype="http://data-vocabulary.org/Breadcrumb">
                <span itemprop="title">確認画面</span>
        </li>
        <li itemscope="itemscope" itemtype="http://data-vocabulary.org/Breadcrumb">
                <span itemprop="title">完了画面</span>
        </li>
    </ul>

    <div>
        <h1>田中商店</h1>
    </div>
    <div>
        <h2>お問い合わせ</h2>
    </div>
    <br>
        <form action="top.php" method="post">
            <div>
                <div>
                <h1 class="contact-title">お問い合わせ 送信完了</h1>
                </div>
                <div align="center">
                    <p>
                        お問い合わせありがとうございました。
                        <br> 内容を確認のうえ、回答させて頂きます。
                        <br> しばらくお待ちください。
                    </p>
                </div>
            </div>
            <div align="center">
                <input id="submit_button" type="submit" name="submit" value="TOPへ">   
            </div>
        </form>
    </div>
    <div align="center">
        <footer>Copyright &copy; 2018 TANAKA SHOTEN All Rights Reserved.</footer>
    </div>
</body>
</html>