<?php

// get parama
$name = $_POST["name"];
$email = $_POST["email"];
$password = $_POST["password"];
$url = $_POST["url"];
$comment = $_POST["comment"];

// mail, .  operator is concatenation
mail($mailladdress, "subject", "message: " . $name);

// redirect. Http header.
header("location: thanks.php");
