<?php
//https://www.w3schools.com/php/php_mysql_select.asp

echo "<table style = 'border: solid 1px black;'>";
echo "<tr><th>Id</th><th>Name</th><th>Email</th><th>Website</th><th>Comment</th><th>Gender</th>";

class TableRows extends RecursiveIteratorIterator {
	function __construct($it){
		parent::__construct($it, self::LEAVES_ONLY);
		
	}
	
	function current(){
		return "<td style = 'width: 150px;border:1px solid black;'>" . 
	parent::current() . "</td>";
	}
	
	function beginChildren(){
		echo "<tr>";
	}
	
	function endChildren(){
		echo "</tr>" . "\n";
	}
}

$servername = "127.0.0.1";
$username = "root";
$password = "";
$dbname = "Train1";
$dsn = 'mysql:dbname=' . $dbname . ';host=' . $servername;

try{
	$dbh = new PDO($dsn, $username, $password);
	//set error mode to exception
	$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$stmt = $dbh->prepare("SELECT ID, Name, Email, Website, Comment, Gender FROM formt");
	$stmt->execute();
	
	//set the resulting array to associative
	$result = $stmt-> setFetchMode(PDO::FETCH_ASSOC);
	foreach(new TableRows(new RecursiveArrayIterator($stmt->fetchAll())) as $k=>$v){
		echo $v;
	}
	echo "Records extracted successfully";
}
	
	catch (PDOException $e){
		echo $stmt . "<br>" . $e->getMessage();
	}
	$dbh = null;
	echo "</table>";
?>