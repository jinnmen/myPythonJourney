<!DOCTYPE HTML>
<html>
<body>
<h1>Connect to database </h1>
<?php
$servername = "localhost";
$database = "Train1";
$username = "root";
$password = "";

// Create connection

$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection

if (!$conn) {

    die("Connection failed: " . mysqli_connect_error());

}
echo "Connected successfully";
mysqli_close($conn);
?>
</body>
</html>
