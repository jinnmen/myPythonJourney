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
            }
            
            if (empty($_POST["email"])){
                $emailErr = "Email is required";
            } else {
                $email = test_input($_POST["email"]);
            }
            
            if (empty($_POST["website"])){
                $website = "";
            } else {
                $website = test_input($_POST["website"]);
            }
            
            if (empty($_POST["comment"])){
                $comment = "";
            } else {
                $comment = test_input($_POST["comment"]);
            }
            
            if (empty($_POST["gender"])){
                $gender = "";
            } else {
                $gender = test_input($_POST["gender"]);
            }
        }
        
        $name = test_input($_POST["name"]);
        if (!preg_match("/^[a-zA-z] * $/", $name)){
            $nameErr = "Only letters and white space allowed";
        }
        
        $email = test_input($_POST["email"]);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)){
            $emailErr = "Invalid email format";
        }
        
        $website = test_input($_POST["website"]);
        if (!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]/i", $website)){
            $websiteErr = "Invalid URL";
        }
        
        $comment = test_input($_POST["comment"]);
        
        $gender = test_input($_POST["gender"]);
        
        function test_input($data){
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
        }
        
        ?>
        
        <form method = "post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
            Name: <input type = "text" name = "name" value = "<?php echo $name;?>">
            <span class = "error">*<?php echo $nameErr;?></span><br>
            
            E-mail: <input type = "text" name = "email" value = "<?php echo $email;?>">
            <span class = "error">*<?php echo $emailErr;?></span><br>
            
            Website: <input type = "text" name = "website" value = "<?php echo $website;?>">
            <span class = "error"><?php echo $websiteErr;?></span><br>
            
            Comment: <input type = "text" name = "comment" rows = "5" cols = "40" value = "<?php echo $comment;?>"><br>
            
            Gender:
            <input type = "radio" name "gender"
            <?php if (isset($gender) && $gender =="female") echo "checked";?>
            value = "female">Female
            
            <input type = "radio" name "gender"
            <?php if (isset($gender) && $gender =="male") echo "checked";?>
            value = "male"> Male
            
            <input type "radio" name "gender"
            <?php if (isset($gender) && $gender =="other") echo "checked";?>
            value = "other"> Other 
            <span class = "error">* <?php echo $genderErr;?></span>
            <br><br>
            <input type = "submit" name = "submit" value = "Submit">
        </form>
        
    </body>
    
</html>