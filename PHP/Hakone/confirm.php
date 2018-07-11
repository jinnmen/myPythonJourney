<?php

// initial first
$error_lists = [];

// get paramas
$name = $_POST["name"];
$mailaddress = $_POST["mailaddress"];

// valdation for string length more than 10 then error
if (strlen($name) > 10) {
    $error_lists[] = "name string over.";
}

//checks if mail is valid. i.e. has @, . etc
if (!preg_match("/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/", $mailaddress)) {
    $error_lists[] = "mailaddress syntax error.";
}

// error check -> Error on html?
if (!empty($error_lists)) {

    $error_html = "<ul>";
    foreach ($error_lists as $key => $value) {
        $error_html .= "<li>" . $value . "</li>";
    }
    $error_html .= "</ul>";
//Why is there a ' below?
    $html = '
<!DOCTYPE html>
<html lang="jp">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <form action="confirm.php" method="post" name="test">';

    $html .= $error_html;

    $html .= '
    name: <input type="input" name="name" value="" /><br />
    mailaddress: <input type="input" name="mailaddress" value="" /><br />
    <input type="submit" name="submit" value="submit" /><br />
  </form>
</body>
</html>';
     echo $html;
     exit();
}
?>
<!DOCTYPE html>
<html lang="jp">
<!--set language to jp-->
<head>
  <meta charset="UTF-8">
<!--user's visible area of page, almost quick responsive-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
<!--form sends to send.php page, posts the information there, sets name as test -->
  <form action="send.php" method="post" name="test">
    name : <?php echo $name; ?> <br />
    mailaddress : <?php echo $mailaddress; ?> <br />
    <input type="submit" name="submit" value="send" /><br />
  </form>
<!--form sends to input.php page, posts the information there, sets name as test? -->
  <form action="input.php" method="post" name="test">
    <input name="name" type="hidden" value="<?php echo $name; ?>" />
    <input name="mailaddress" type="hidden" value="<?php echo $mailaddress; ?>" />
    <input type="submit" name="submit" value="back" />
  </form>

</body>
</html>
