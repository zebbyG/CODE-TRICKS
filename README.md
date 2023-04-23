+ [x] CODE-TRICKS

`RUN ANY FILE`

`Fibonacci.py`
+ [x] To print Fibonacci numbers
  + To run it: `python3  Fibonacci.py`

`FizzBuzz.py`
+ [x] To print 'Fizz', 'Buzz' and 'FizzBuzz' according to the conditions.
  + To run it: `python3 FizzBuzz.py`

`triangle_area.py`
+ [x] To calculate the area of a triangle
  + To run it: `python3 triangle_area.py`

`meta.py`
+ [x] To draw the meta logo
  + To run it `python3 meta.py`

`type_anywhere.py`
+ [x] To print statement * number_of_times with delays after each statements. All inputs.
  + To run it `python3 type_anywhere.py` after the program prints after what time it will start, navigate anywhere on your machine where you want the statements to be printed and see the magic of pyautogui module.

`random_1v1.py`
+ [x] A game where you choose attacks on your random enemies until one of you is dead `life < 1`. Enemies launch attacks after you attack. Every attack has an impact unless otherwise.
  + To run it `python3 random_1v1.py`

`sketch.py`
+ [x] To sketch anything using the `sketchpy` python module.
  + import the module `from sketchpy import library`
  + `library.get_arts()` returns all available arts in the library
  + To draw from a `SVG` file:
    + `from sketchpy import canvas`
    + Assign a variable to `canvas.draw_from_svg('FILE PATH')` then call the draw function `variable_name.draw()`
  + To draw from a `raw` image:
    + `from sketchpy import canvas`
    + Assign a variable to `canvas.sketch_from_image('IMAGE PATH')` then call the draw function `variable_name.draw()`

Arguments that can be added to the `draw()` function in the `sketchpy` library depend on the specific `class` or `function` being used to generate the canvas and drawing