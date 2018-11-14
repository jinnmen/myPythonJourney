<?php

namespace App\Http\Requests;

use Illumuniate\Contracts\Validation\Validator;

trait ConfirmRequestTrait
{
	/**
	* Set custom messages for validator errors.
	*
	*@param \Illuminate\Contracts\Validation\Factory $factory
	*
	*@return \Illuminate\Contracts\Validation\Validator
	*/

	public function validator($factory)
	{
		// Process before verification
		if (method_exists($this, 'beforeValidate')){
			$this->beforeValidate();
		}
		
		//Add validation for confirmation screen flag
		$rules = array_merge($this->rules(),[
			'confirming' => 'required|accepted',
		]);

		$validator = $factory->make(
			$this->all(),
			$rules,
			$this->messages(),
			$this->attributes()
		);

		$validator->after(function ($validator){
			$failed = $validator->failed();

			//Exclude validation of confirmation screen flag
			unset($failed['confirming']);

			// If no error other than confirmation screen flag, display confirmation screen
			if (count($failed)=== 0){
				$this->merge(['confirming' => 'true']);
			}

			// Processing after value verification
			if (method_exists($this, 'afterValidate')){
				$this->afterValidate($validator);
			}

		});

		return $validator;

	}

	/**
	* Format the errors from the given Validator instance.
	*
	*@param \Illuminate\Contracts\Validation\Validator $validator
	*
	* @return array
	*/
	protected function formatErrors(Validator $validator)
	{
		$errors = parent::formatErrors($validator);

		// Delete confirmation display flag error message
		unset($errors['confirming']);

		return $errors;
	}

}