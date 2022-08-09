<?php
$fname=basename($_REQUEST['filename']);
file_put_contents('upload/' . $fname, file_get_contents('php://input'));
?>
