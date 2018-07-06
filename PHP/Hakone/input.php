<?php

/// init
$name = "";
$mailaddress = "";

// get params
if (!empty($_POST["name"])) {
    $name = $_POST["name"];
}
if (!empty($_POST["mailaddress"])) {
    $mailaddress = $_POST["mailaddress"];
}
?>

<!DOCTYPE html>
<html lang="jp">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <form action="confirm.php" method="post" name="test">
    name: <input type="input" name="name" value="<?php echo $name; ?>" /><br />
    mailaddress: <input type="input" name="mailaddress" value="<?php echo $mailaddress; ?>" /><br />
    <input type="submit" name="submit" value="submit" /><br />
  </form>
</body>
</html>
