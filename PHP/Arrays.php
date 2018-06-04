<html>
  <head>
    <title>Woot, More Arrays!</title>
  </head>
  <body>
    <p>
      <?php
        // Add your array elements after
        // "Beans" and before the final ")"
        $array = array("Egg", "Tomato", "Beans", "Chips", "Sausage" );        
      ?>
    </p>
  </body>
</html>

<html>
  <head>
    <title>My First Array</title>
  </head>
  <body>
    <p>
      <?php
        $friends = array("a", "b", "c");
      ?>
    </p>
  </body>
</html>

# 3rd item

<html>
  <head>
    <title>Accessing Elements</title>
  </head>
  <body>
    <p>
      <?php
        $tens = array(10, 20, 30, 40, 50);
        echo $tens[2];
      ?>
    </p>
  </body>
</html>


<html>
  <head>
    <title>Leap Years</title>
  </head>
  <body>
    <?php
      for ($leap = 2004; $leap < 2050; $leap = $leap + 4) {
        echo "<p>$leap</p>";
      }
    ?>
  </body>
</html>