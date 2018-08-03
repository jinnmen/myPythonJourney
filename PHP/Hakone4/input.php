<?php

$name = "";
$email = "";
$password = "";
$url = "";
$comment = "";

if (!empty($_POST["name"])){
	$name = $_POST["name"];
}

if (!empty($_POST["email"])){
	$email = $_POST["email"];
}

if (!empty($_POST["password"])){
	$password = $_POST["password"];
}

if (!empty($_POST["passcheck"])){
	$form_check_1 = $_POST["passcheck"];
}

if (!empty($_POST["url"])){
	$url = $_POST["url"];
}

if (!empty($_POST["comment"])){
	$comment = $_POST["comment"];
}

?>



<!doctype html>
<!-- http://54.199.142.88/bs/bsform.php
Grid: https://getbootstrap.com/docs/4.1/layout/grid/
-->

<html lang = "en">
   <head>
<!--html formatter: https://www.freeformatter.com/html-formatter.html#ad-output -->
      <meta charset = "utf-8">
      <meta name = "viewport" content = "width = device-width, initial-scale = 1, shrink-to-fit = no">
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
      <title> Form with BS </title>
   </head>
   <body>
		 <form action = "confirm.php" method = "post" name = "confirmed">
	  <div class = "container">

      <div class = "row">
         <div class = "col-md-2"></div>
      </div>
      <form method = "post" name = "test">
         <div class = "row justify-content-center">
            <div class = "col-md-8">

              <div class="form-group">
                <div class = "row justify-content-center">
      			 <h1> Hello, BS world! </h1>
              	</div>

              	<div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="name">Name</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="input" name = "name" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Enter Name" value= "<?php echo $name; ?>">

                 </div>
                 </div>



              	<div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="email">Email address</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="input" name= "email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email" value= "<?php echo $email; ?>" />
                 <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                 </div>
                 </div>


              <div class = "row justify-content-center">
              <div class = "col-md-4">
              <label for="password">Password</label>
              </div>

              <div class = "col-md-4">
              <input type="password" name = "password" class="form-control" id="password" placeholder="Password" value= "<?php echo $password; ?>" />

              <div class="form-group form-check">
                <input type="checkbox" name= "passcheck" class="form-check-input" id="passcheck" value = "<?php if(isset($_POST['passcheck'])) echo "checked"; ?>" />
                <label class="form-check-label" for="passcheck">Agree to T&Cs</label>
                </div>
                </div>

								 </div>      <!--Closing for row justify content center -->

              	<div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="url">Website URL</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="url" name = "url" class="form-control" id="url" aria-describedby="urlHelp" placeholder="Enter URL" value= "<?php echo $url; ?>" />

                 </div>
                 </div>

                <div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="comment">Comment</label>
                 </div>

                 <div class = "col-md-4">
                 <textarea name = "comment" class="form-control" rows="3" id="comment" aria-describedby="commentHelp" placeholder="Enter Comment"><?php echo $comment; ?> </textarea>

                 </div>
                 </div>


								 <br />

              <div class = "row justify-content-center">
              <button type="submit" class="btn btn-primary">Submit</button>
              </div>
						</div> <!-- closing for form-group -->
           </div> <!--closing for col md 8 -->
         </div>
      </form>
      <div class = "row">
         <div class = "col-md-2"></div>
      </div>

      </div>
		</form>
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
   </body>
</html>
