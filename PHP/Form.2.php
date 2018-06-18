/* https://www.w3schools.com/php/php_form_validation.asp */
<!DOCTYPE html>
<html>
    <head>
        <title>Form test</title>
    </head>
    <body>
        <?php
        // define variables and set to empty values
        $nameErr = $emailErr = $genderErr = $websiteErr = "";
        $name = $email = $gender = $comment = $website = "";
        
        if ($_SERVER["REQUEST_METHOD"] == "POST"){
            if (empty($_POST["name"])){
                $nameErr = "Name is required";
            } else {
                $name = test_input($_POST["name"]);
                // check if name only contains letters and whitespace
                if (!preg_match("/^[a-zA-Z ]*$/", $name)){
                    $nameErr = "Only letters and white space allowed";
                }
            }
            
            if (empty($_POST["email"])){
                $emailErr = "Email is required";
            } else {
                $email = test_input($_POST["email"]);
                // check if e-mail address is well-formed
                if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
                    $emailErr = "Invalid email format";
                }
            }
            
            if (empty($_POST["website"])){
                $website = "";
            } else {
                // check if website is valid (this regex also allows dashes in the URL)
                $website = test_input($_POST["website"]);
                if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i",$website)) {
  $websiteErr = "Invalid URL"; 
                }
            }
            
            if (empty($_POST["comment"])){
                $comment = "";
            } else {
                $comment = test_input($_POST["comment"]);
            }
            
            if (empty($_POST["gender"])){
                $genderErr = "Gender is required";
            } else {
                $gender = test_input($_POST["gender"]);
            }
        }
        
         function test_input($data){
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
        }
       
        ?>
        
        <h2>PHP Form Validation Example</h2>
        <p><span class = "error">* required field</span></p>
        
        <form method = "post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            Name: <input type = "text" name = "name" value = "<?php echo $name; ?>">
            <span class = "error">* <?php echo $nameErr;?></span><br>
            
            E-mail: <input type = "text" name = "email" value = "<?php echo $email; ?>">
            <span class = "error">* <?php echo $emailErr;?></span><br>
            
            Website: <input type = "text" name = "website" value = "<?php echo $website; ?>">
            <span class = "error"><?php echo $websiteErr;?></span><br>
            
            Comment: <textarea name = "comment" rows = "5" cols = "40"><?php echo $comment;?></textarea><br>
            
            Gender:
            <input type = "radio" name = "gender" <?php if (isset($gender) && $gender == "female") echo "checked";?> value = "female"> Female
            <input type = "radio" name = "gender" <?php if(isset($gender) && $gender == "male") echo "checked"; ?> value = "Male"> Male
            <input type = "radio" name = "gender" <?php if(isset($gender) && $gender =="other") echo "checked"; ?>value = "other"> Other
            <span class = "error">* <?php echo $genderErr;?></span>
            <br><br>
            
        	<input type = "submit" name = "submit" value = "Submit" />
        </form>
        
        <?php
        echo "<h2>Your Input:</h2>";
        echo "<br>";
        echo $name;
        echo "<br>";
        echo $email;
        echo "<br>";
        echo $website;
        echo "<br>";
        echo $comment;
        echo "<br>";
        echo $gender;
        ?>
        
        <?php
        /*Email from php: https://www.w3schools.com/php/func_mail_mail.asp */
        
        // the message
        $msg = "Name: $name \nEmail: $email \nWebsite: $website \nComment: $comment \nGender: $gender";
        
        //use wordwrap() if lines are longer than 70 chars
        $msg = wordwrap ($msg, 70);
        
		// send email
		mail("jinnmen.leong@plan-b.co.jp", "Test PHP mail", $msg);        
        ?>
        
        
		<?php
		// go to thank you page
		if (isset($_POST['submit'])){
  		header("Location: thanks.php");
		}
		?>

		
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
		
		$sql =  "INSERT INTO TableName (name, email, website, comment, gender)
		VALUES ($name, $email, $website, $comment, $gender)";
		
		if ($connect -> query($sql) === TRUE){
		    echo "New record created successfully";
		} else {
		    echo "Error: " . $sql . "<br>" . $connect-> error; 
		}
		
		$connect -> close();
		/*
		// Send to database: https://www.jotform.com/help/126-How-to-send-Submissions-to-Your-MySQL-Database-Using-PHP
		function ExtendedAddslash(&$params)
		{
			foreach($params as &$var){
				is_array($var) ?ExtendedAddslash($var): $var = addslashes($var);
				unset($var);
			}
		}
		
		ExtendedAddslash($_POST);
		
		$submission_id = $_POST['submission_id'];
		$formID = $_POST['formID'];
		$ip = $_POST['ip'];
		$name = $_POST['name'];
		$email = $_POST['email'];
		$website = $_POST['website'];
		$comment = $_POST['comment'];
		$gender = $_POST['gender'];
		
		$db_host = '127.0.0.1';
		$db_username = 'root';
		$db_password = '';
		$db_name = 'Train1';
		
		mysql_connect($db_host, $db_username, $db_password) or die(mysql_error());
		mysql_select_db($db_name);
		
		$query = "SELECT * FROM `formt` WHERE `submission_id` = '$submission_id'";
		$sqlsearch = mysql_query($query);
		$resultcount = mysql_numrows($sqlsearch);
		
		if(resultcount > 0){
		
			mysql_query("UPDATE `table_name` SET
						`name` = '$name',
						`email` = '$email',
						`website` = '$website',
						`comment` = '$comment',
						`gender` = '$gender'
					WHERE `submission_id` = '$submission_id'")
			or die(mysql_error());
			
		} else{
			
			mysql_query("INSERT INTO `table_name`(submission_id, formID, IP, name, email, website, comment, gender)
						VALUES ('$submission_id', '$formID', '$ip', '$name', '$email', '$website', '$comment', '$gender')")
					or die(mysql_error());
		}
		*/
		?>

		<?php
		// Selecting from database: https://www.w3schools.com/php/php_mysql_select.asp
		$servername = "127.0.0.1";
		$username = "root";
		$password = "";
		$dbname = "Train1";
		
		$connect = mysqli_connect($servername, $username, $password, $dbname);
		if (!$connect){
		    die("Connection failed!: ".$connect->connect_error);
		} 
		
		$sql =  "SELECT name, email, website, comment, gender FROM tablename";
		$result = mysqli_query($connect, $sql);
		
		// TBC
		
		?>


    </body>
    
</html>