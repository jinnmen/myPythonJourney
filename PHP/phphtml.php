<?php 

$error_lists = [];

if (strlen($str) > 5) {
    $error_lists[] = "string error.";  
} 
if (!preg_match('/@/', $mailaddress)) {
    $error_lists[] = "mailadress error.";  
}

if (empty($error_lists) === false) {
    // is error
    $error_html = '<html><body>';
    foreach ($error_lists as $key => $value) {
      $error_html .= '<li>' . $value . '</li>';
    } 
    $error_html .= '</body></html>';
    echo $error_html;
    exit();
}

<html>
<body>
<li>string error</li>
<li>mailaddress error</li>
</body>
