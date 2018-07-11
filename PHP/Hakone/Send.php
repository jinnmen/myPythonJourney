<?php

// get parama
$name = $_POST["name"];
$mailaddress = $_POST["mailaddress"];

// mail
mail($mailladdress, "subject", "message: " . $name);

// redirect. Http header.
header("location: thnks.php");
