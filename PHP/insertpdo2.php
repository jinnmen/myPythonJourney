<?php
session_start();
?>

<?php
//https://www.w3schools.com/php/php_mysql_insert.asp
$servername = "127.0.0.1";
$username = "root";
$password = "";
$dbname = "Train1";
$dsn = 'mysql:dbname=' . $dbname . ';host=' . $servername;

try{
	$dbh = new PDO($dsn, $username, $password);
	//set error mode to exception
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$sql =  "INSERT INTO formt (Name, Email, Website, Comment, Gender)
		VALUES (" . $_SESSION['name'] . "," . $_SESSION['email'] . "," . $_SESSION['website'] . "," . $_SESSION['comment'] . "," . $_SESSION['gender'] . ")";
		var_dump($sql);
		die();
	//use exec() because no results are returned
	$dbh->exec($sql);
	echo "New record created successfully";
	}catch (PDOException $e){
		echo $sql . "<br>" . $e->getMessage();
	}
	$dbh = null;
?>