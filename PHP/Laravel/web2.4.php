<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
dd = die and dump task. Allows ID and details to be shown in browser when key in "blog.test/tasks/1 or 2 or 3"
*/

Route::get('/', function () {

	$tasks = DB::table('tasks')->latest()->get();

	return view('welcome',compact('tasks'));

});


Route::get('/tasks/{task}', function ($id){

	$task = DB::table('tasks')->find($id);

	dd($task);

	return view('welcome', compact('tasks'));

});