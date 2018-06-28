<?php
	echo "Here are my files";
	$path = ".";
	$dh = opendir($path);
	$i = 1;
	while (($file = readdir($dh)) !== false){
		if($file != "." && $file != ".." && $file != "index.php" && $file != ".htaccess" && $file != "cgi-bin"){
			echo "<a href='$path/$file'>$file</a><br /><br />";
			$i++;
		}
	}
closedir($dh);
?>