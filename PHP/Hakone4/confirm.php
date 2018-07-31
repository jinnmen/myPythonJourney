<?php

// initial first
$error_lists = [];

// get paramas
$name = $_POST["name"];
$email = $_POST["email"];
$password = $_POST["password"];
$url = $_POST["url"];
$comment = $_POST["comment"];

// valdation for string length more than 10 then error
if (strlen($name) > 10) {
    $error_lists[] = "name string over.";
}

//checks if mail is valid. i.e. has @, . etc
if (!preg_match("/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/", $email)) {
    $error_lists[] = "mailaddress syntax error.";
}

//checks url
if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$url)) {
  $error_lists[] = "Invalid URL";
}

// if empty is true return error lists.
if (!empty($error_lists)) {

    $error_html = "<ul>";
    foreach ($error_lists as $key => $value) {
        $error_html .= "<li>" . $value . "</li>";
    }
    $error_html .= "</ul>";
//saves whole chunk from DOCTYPE to test within $html var
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
  <form action="confirm.php" method="post" name="test">'; //ends here

//Appends $error_html to $html with .= operator
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

?> <!-- end of top php tag-->

<!DOCTYPE html>
<html lang="jp">
<!--set language to jp-->
<head>
  <meta charset="UTF-8">
<!--user's visible area of page, almost quick responsive-->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
<div class = "container">
  <div class = "col-md-2">
  </div>

<!--Button for form sends to send.php page, posts the information there, sets name as test -->
  <form action="send.php" method="post" name="test">
    Name : <?php echo $name; ?> <br />
    Email : <?php echo $email; ?> <br />
    Password: <?php echo $password ;?> <br />
    $url : <?php echo $url; ?> <br />
    $comment: <?php echo $comment ?> <br />
    <input type="submit" name="submit" value="send" /><br />
  </form>
<!--Button for form sends to input.php page, posts the information there, sets name as test? -->
  <form action="input.php" method="post" name="test">
    <input name="name" type="hidden" value="<?php echo $name; ?>" />
    <input name="email" type="hidden" value="<?php echo $email; ?>" />
    <input name="password" type ="hidden" value = "<?php echo $password; ?>" />
    <input name="url" type = "hidden" value = "<?php echo $url; ?>" />
    <input name ="comment" type = "hidden" value = "<?php echo $comment; ?>" />
    <input type="submit" name="submit" value="back" />

    <div class = "col-md-2">
    </div>

  </div>
  </form>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
</body>
</html>
