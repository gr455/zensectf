<style>
body {
  background-image: url(hackerman.jpg);
  color: white;
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>

<body>
<?php
error_reporting(0);
ini_set('display_errors', 0);

if (isset($_POST['username']) && isset($_POST['username'])) {
  $connect = mysql_connect('localhost','ctf','Jie2Roh8ohre3Ahn');
  mysql_select_db("ctf") or die("unable to find db.. I am broken.");

  if( $connect === FALSE ) {
    die('Cannot connect to db, I am broken.');
  }
  $username = $_POST['username'];
  $password = $_POST['password'];

  $query = "SELECT username FROM users WHERE username='$username' AND password = '$password'";
  $result = @mysql_query($query) or die(mysql_error());

  if( mysql_num_rows($result) === 0 ) {
    die('<h3>Invalid login or password</h3>');
  }
  elseif( mysql_num_rows($result) > 1 ) {
    die('<h3>So you\'re telling me, you are ' . strval(mysql_num_rows($result)) . ' people at one time?</h3><h2>GO AWAY</h2>');
  }
  else {
    die('<h3>zenseCTF{u5E_pr3P4red_QueR1es_nex7_tiM3}</h3>');
  }
}
?>
<h1>Welcome to My Secure and Quick Login</h1>
<form action="" method="post">
  <input type="text" name="username" placeholder="username" />
  <input type="password" name="password" placeholder="password"/>
  <button type="submit">Login</button>
</form>
</body>