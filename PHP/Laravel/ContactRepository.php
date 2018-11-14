<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class RepositoryServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }

    /**
     * Register services.
     *
     * @return void
     */
    public function register()
    {
        $repositories = [
            \App\Repositories\ContactRepository::class,
        ];

        foreach ($repositories as $repository){
            $this->app->bind($repository, $repository.'Eloquent');
        }
        //
    }
}
