<!DOCTYPE HTML>
<html>
<body>

		<?php
		//https://www.w3schools.com/php/php_mysql_insert.asp
		$servername = "127.0.0.1";
		$username = "root";
		$password = "";
		$dbname = "Train1";
		
		$connect = new mysqli($servername, $username, $password, $dbname);
		if ($connect->connect_error){
		    die("Connection failed!: ".$connect->connect_error);
		} 
		
		$sql =  "INSERT INTO formt (Name, Email, Website, Comment, Gender)
		VALUES (" . $name . "," . $email . "," . $website . "," . $comment . "," . $gender . ")";
		var_dump($sql);
		die();
		
		if ($connect -> query($sql) === TRUE){
		    echo "New record created successfully";
		} else {
		    echo "Error: " . $sql . "<br>" . $connect-> error; 
		}
		
		$connect -> close();

		?>

</body>
</html>