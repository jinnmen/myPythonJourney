<?php

/// init. "" = String goes in. If int start with 0 or null or []. 
$name = "";
$mailaddress = "";
$url = "";
$comment1 = "";
$comment2 = "";

// Check if its empty. If empty, return true. Else return false. $_POST Environment. Will run when return/back from next page. 
if (!empty($_POST["name"])) {
    $name = $_POST["name"];
}
if (!empty($_POST["mailaddress"])) {
    $mailaddress = $_POST["mailaddress"];
}
if (!empty($_POST["url"])){
	$url = $_POST["url"];
}
if (!empty($_POST["comment1"])){
	$comment1 = $_POST["comment1"];
}
if (!empty($_POST["comment2"])){
	$comment2 = $_POST["comment2"];
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
  <!--prints html "url", then allows input, name and value. Then echos url in php -->
	website url: <input type = "input" name = "url" value ="<?php echo $url ; ?>" /><br />
  <!--prints html "comment", then allows input, name and value. Then echos comment in php . input type only shows 1 row-->
	comment1: <input type = "input"  name = "comment1" rows = "5" cols = "40" value= "<?php echo $comment1 ; ?>" /><br />
  <!--prints html "comment", then allows input, name and value. Then echos comment in php . textarea shows text box but need to close bracket early. no need to use value-->
	comment2: <textarea name = "comment2" rows = "5" cols = "40"> <?php echo $comment2 ;?> </textarea> <br />
  <!--shows submit button, then saves name and value. -->
    <input type="submit" name="submit" value="submit" /><br />

  </form>
</body>
</html>
