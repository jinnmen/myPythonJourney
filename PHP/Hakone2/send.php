<?php

// get parama
$name = $_POST["name"];
$mailaddress = $_POST["mailaddress"];
$url = $_POST["url"];
$comment1 = $_POST["comment1"];
$comment2 = $_POST["comment2"];

// mail, .  operator is concatenation
mail($mailladdress, "subject", "message: " . $name);

// redirect. Http header.
header("location: thanks.php");
