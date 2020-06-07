<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
form {border: 3px solid #f1f1f1;}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}
</style>
</head>
<body>

  <link rel='stylesheet' href='assets/css/bootstrap.min.css'>
  <link rel='stylesheet' href='assets/css/animate.min.css'>
  <link rel='stylesheet' href="assets/css/font-awesome.min.css"/>
  <!-- <link rel='stylesheet' href="assets/css/style.css"/> -->
  
  <!-- Fonts -->
  <link href='http://fonts.googleapis.com/css?family=Raleway:200,300,400,500,600,700,800' rel='stylesheet' type='text/css'>

  <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
  <![endif]-->
      
  <!-- Favicon -->
  <link rel="shortcut icon" href="#">
</head>
<body>
<!-- Begin Hero Bg -->
<div id="parallax">
</div>
<!-- End Hero Bg
  ================================================== -->
<!-- Start Header
  ================================================== -->
<header id="header" class="navbar navbar-inverse navbar-fixed-top" role="banner" style="height: 18%">
<div class="container">
  <div class="navbar-header">
    <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".bs-navbar-collapse">
    <span class="sr-only">Toggle navigation</span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
    </button>
    <!-- Your Logo -->
    <!-- <a href="#hero" class="navbar-brand">THE WHITEROSE <span class="lighter">FOUNDATION</span></a> -->
    <img src="assets/img/text.png" width="30%" height="30%">
  </div>
  <!-- Start Navigation -->
  <nav class="collapse navbar-collapse bs-navbar-collapse navbar-right" role="navigation">
  <ul class="nav navbar-nav">
    <li>
    <a href="index.php">Home</a>
    </li>
    <li>
    <a href="index.php#about">About</a>
    </li>
    <li>
    <a href="/login.php">Login</a>
    </li>
  </ul>
  </nav>
</div>
</header>


<div style="padding-top: 10%;">
<h2 align="center">Superusers only login</h2>
<form action="/action_page.php" method="post">
  <div class="imgcontainer">
    <img src="assets/img/text2.png" alt="Avatar" class="non" width="30%" height="30%">
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>
        
    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
  </div>
</form>
</div>

</body>
</html>
