<!DOCTYPE html>
<html>
<head>
	<title>Bootstrap test</title>
	<link rel="stylesheet" type="text/css" href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
	<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
   <script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
	<h1>Import a txt file</h1>
<form role="form" class="flp" action="index.php" method="post" enctype="multipart/form-data">
	<div class="form-group">
		
		<input type="file" name="file" id="file"/>
	</div>
	<div class="form-group">
	<button type="submit" class="btn btn-default">submit</button>
</div>
</form>

<?php
if ($_FILES["file"]["error"] > 0||($_FILES["file"]["type"] == "text/txt"))
    {
    echo "erro: " . $_FILES["file"]["error"] . "<br />";
    }
else if($_FILES["file"])
    {
    echo "<div class='text'>filename: " . $_FILES["file"]["name"] . "<br />";
    echo "type: " . $_FILES["file"]["type"] . "<br />";
    echo "size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
    echo "location: " . $_FILES["file"]["tmp_name"].'</div>';
    
    if (file_exists("upload/" . $_FILES["file"]["name"]))
        {
          echo "<div class='text'>".$_FILES["file"]["name"] . " file exist.</div>";
        }
    else
        {
          move_uploaded_file($_FILES["file"]["tmp_name"],
          "upload/" . $_FILES["file"]["name"]);
          echo "<div class='text'>file moved to" . " upload/" . $_FILES["file"]["name"]."</div>";
        } 
    // $tmp=shell_exec('ping -c 1 localhost');
    $tmp=shell_exec('python word_freq.py upload/'.$_FILES["file"]["name"]);
    echo $tmp;

    $filename="test.dat";
    }
?> 

 </body>