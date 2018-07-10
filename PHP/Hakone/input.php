<?php

/// init
$name = "";
$mailaddress = "";

// get params, why if empty Post? If send empty will be empty? If refresh page info won't dissapear.
if (!empty($_POST["name"])) {
    $name = $_POST["name"];
}
if (!empty($_POST["mailaddress"])) {
    $mailaddress = $_POST["mailaddress"];
}
?>

<!DOCTYPE html>
<html lang="jp">
<!--set language to jp-->
<head>
  <meta charset="UTF-8">
  <!--user's visible area of page, almost quick responsive-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- setting header to php, compatible with ie edge-->
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
<!--form sends to confirm.php page, posts the information there, sets name as test -->
  <form action="confirm.php" method="post" name="test">
  <!--prints html "name", then allows input, name and value. Then echos name in php -->
    name: <input type="input" name="name" value="<?php echo $name; ?>" /><br />
  <!--prints html "mailaddress", then allows input, name and value. Then echos mailaddress in php -->
    mailaddress: <input type="input" name="mailaddress" value="<?php echo $mailaddress; ?>" /><br />
  <!--shows submit button, then saves name and value. -->
    <input type="submit" name="submit" value="submit" /><br />
  </form>
</body>
</html>
