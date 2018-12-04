<!-- create.blade.php -->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Index Page </title>
    <link rel="stylesheet" href="{{asset('css/app.css')}}">
  </head>
  <body>
  	<div class ="container">
  	<br />
  	@if (\Session::has('success'))
  		<div class="alert alert-success">
  			<p>{{ \Session::get('success')}}</p>
  		</div><br />
  	@endif
  	<table class="table table-striped">
  	<thread>
  		<tr>
  			<th>ID</th>
  			<th>CoinName</th>
  			<th>CoinPrice</th>
  			<th colspan="2">Action</th>
  		</tr>
  	</thread>
  	<tbody>
  		@foreach($forms as $form)
  		<tr>
  			<td>{{$form['id']}}</td>
  			<td>{{$form['coinname']}}</td>
  			<td>{{$form['coinprice']}}</td>
  			<td><a href="{{action('FormController@edit', $form['id'])}}" class = "btn btn-warning">Edit</a></td>
  			<td>
  				<form action="{{action('FormController@destroy', $form['id'])}}" method="post">
  					{{csrf_field()}}
  					<input type="hidden" name="method" value="DELETE">
  					<button class="btn btn-danger" type="submit">DELETE</button>
  				</form>
  			</td>
  		</tr>
  		@endforeach
  	</tbody>
  </table>
</div>
</body>
</html>