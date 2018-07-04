<?php
//Validating from myform, https://myphpform.com/validating-forms.php

$yourname = check_input ($_POST['yourname'], "Enter your name!");
$email = check_input ($_POST['email'], "Enter your email!");
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