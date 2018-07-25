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
	  <div class = "container">

      <div class = "row">
         <div class = "col-md-2"></div>
      </div>
      <form>
         <div class = "row justify-content-center">
            <div class = "col-md-8">

              <div class="form-group">
                <div class = "row justify-content-center">
      			 <h1> Hello, BS world! </h1>
              	</div>

              	<div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="nameInput">Name</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="name" class="form-control" id="nameInput" aria-describedby="nameHelp" placeholder="Enter Name" value= "<?php echo $name; ?>">

                 </div>
                 </div>



              	<div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="emailInput">Email address</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="email" class="form-control" id="emailInput" aria-describedby="emailHelp" placeholder="Enter email">
                 <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                 </div>
                 </div>


              <div class = "row justify-content-center">
              <div class = "col-md-4">
              <label for="passwordInput">Password</label>
              </div>

              <div class = "col-md-4">
              <input type="password" class="form-control" id="passwordInput" placeholder="Password">

              <div class="form-group form-check">
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Agree to T&Cs</label>
                </div>
                </div>

              	<div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="urlInput">Website URL</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="url" class="form-control" id="urlInput" aria-describedby="urlHelp" placeholder="Enter URL">

                 </div>
                 </div>

                <div class = "row justify-content-center">
              	<div class = "col-md-4">
                 <label for="commentInput">Comment</label>
                 </div>

                 <div class = "col-md-4">
                 <input type="comment" class="form-control" id="commentInput" aria-describedby="commentHelp" placeholder="Enter Comment">

                 </div>
                 </div>

              </div>      <!--Closing for row justify content center -->


              <div class = "row justify-content-center">
              <button type="submit" class="btn btn-primary">Submit</button>
              </div>
							</div>
           </div> <!--closing for col md 8 -->
         </div>
      </form>
      <div class = "row">
         <div class = "col-md-2"></div>
      </div>

      </div>
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
   </body>
</html>
