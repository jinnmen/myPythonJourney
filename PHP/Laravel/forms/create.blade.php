<DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Form creation Laravel test</title>
		<link rel="stylesheet" href="{{asset('css/app.css')}}">
	</head>
	<body>
		<div class="container">
			<h2>Create A Form</h2><br />
			<form method="post"> <!-- This method attribute of the form element tells the web browser to send form data to a server. Specifying a value of POST means the browser will send the data to the web server to be processed.-->
				<div class="row">
					<div class="col-md-4"></div>
						<label for = "Name"> Name: </label>
						<input type = "text" class="form-control" name = "name">
					</div>
				</div>
				<div class="row">
					<div class="col-md-4"></div>
						<div class="form-group col-md-4">
							<label for = "Email"> Email: </label>
							<input type= "email" class = "form-control" name = "email">
						</div>
					</div>
				</div>
				<div class="row">
					<div class="col-md-4"></div>
						<div class="form-group col-md-4">
							<label for = "Password"> Password: </label>
							<input type = "password" class= "form-control" name = "password">
						</div>
					</div>
				</div>
				<div class="row">
					<div class="col-md-4"></div>
						<div class="form-group col-md-4">
							<label for = "PhoneNumber"> Phone Number: </label>
							<input type = "number" class = "form-control" name = "phonenumber">
						</div>
					</div>
				</div>
				<div class="row">
					<div class = "col-md-4"></div>
						<div class="form-group col-md-4">
							<label for = "Comments"> Comments: </label>
							<textarea class = "form-control" rows= "5" name = "comments"></textarea> 
						</div>
					</div>
				</div>

			<div class ="row">
				<div class="col-md-4"></div>
					<div class="form-group col-md-4">
						<button type="submit" class="btn btn-success" style = "margin-left: 38px"> Submit</button>
					</div>
				</div>
			</form>
		</div>
	</body>
</html>