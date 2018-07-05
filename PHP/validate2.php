<?php
//Validating from myform, https://myphpform.com/validating-forms.php

$yourname = check_input ($_POST['yourname'], "Enter your name!");
$email = check_input ($_POST['email'], "Enter your email!");
$email = htmlspecialchars($_POST['email']);
if (!preg_match("/([\w\-]+[\w\-]+\.[\w\-]+)/", $email))
{
	die("E-mail address not valid");
}
$url = check_input($_POST['url'], "Enter a valid URL");
$url = htmlspecialchars($_POST['website']);
if (!preg_match("/^(https?:\/\/+[\w\-]+[\w\-]+/i)",$url))
{
	die("URL address not valid");
}
$likeit = check_input ($_POST['likeit'], "Choose one!");
$comments = check_input ($_POST['comments'], "Key in something!");
?>

<html>
<body>

Your name is: <?php echo $yourname; ?><br />
Your e-mail: <?php echo $email; ?><br />
<br />

Do you like this website? <?php echo $likeit; ?><br />
<br />

Comments: <br />
<?php echo $comments; ?>

</body>
</html>

<?php
function check_input($data, $problem =''){
	$data = trim($data);
	$data = stripslashes($data);
	$data = htmlspecialchars($data);
	if ($problem && strlen($data) == 0){
		show_error($problem);
	}
	return $data;
}

function show_error($myError){
	
	echo "<br/><b>Please correct the following error: </b> <br/>";
	echo $myError;
	
//exit();
}
?>