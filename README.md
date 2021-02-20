# ANSI Beautifier

This is a beautifier project to beautify your python command-line or GUI applications.

It uses ANSI Escape codes (\u001b) to color the text.

# Installation
``` Python
pip install ansibeautifier
```

# Usage
``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.red(text="Hello World", bright=False))
```

Returns <span style="color: red;">Hello World</span> in red but not bright as we have given the bright=False parameter

The default bright parameter is False.


# Variable Usage

You can also store the colored text in a variable
``` Python
from ansibeautifier import Beautifier
b = Beautifier()
text = b.green(text="Hello World", bright=False)
print(text)
```

This also prints the same result but in a pythonic way!

# Colors supported

1. Green - ansibeautifier.Beautifier.green()
2. Red - ansibeautifier.Beautifier.red()
3. Blue - ansibeautifier.Beautifier.blue()
4. Black - ansibeautifier.Beautifier.black()
5. White - ansibeautifier.Beautifier.white()
6. Yellow - ansibeautifier.Beautifier.yellow()
7. Magenta - ansibeautifier.Beautifier.magenta()
8. Cyan - ansibeautifier.Beautifier.cyan()

# Other functions

1. ansibeautifier.Beautifier.always_<color_name>()

It colors the terminal in which you run the python code. It can be reset by using the ansibeautifier.Beautifier.reset_foreground_color() function

``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.always_white(text="Hello World"))
print(b.reset_foreground_color())
```

2. ansibeautifier.Beautifier.background_<color_name>()

It colors the background of the text to the color specified
It can be nullified by the ansibeautifier.Beautifier.reset_background_color() function

``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.background_black(text="Hello World", bright=True))
print(b.reset_colors())
```

3. ansibeautifier.Beautifier.always_background_<color_name>()

It colors the background of the terminal and the text specified

``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.always_background_cyan(text="Hello World"))
print(b.reset_colors())
```

4. ansibeautifier.Beautifier.bold()

It returns bold text. It can be neutralized by the ansibeautifier.Beautifier.reset_intensity() function.

``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.bold(text="Hello World"))
print(b.reset_intensity())
```

It returns <b>Hello World</b>

5. ansibeautifier.Beautifier.underline()

It returns underlined text. It can also be neutralized by the ansibeautifier.Beautifier.reset_intensity() function.

``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.underline(text="Hello World", always=True))
print(b.reset_intensity())
```
This underlines all the text in the terminal and the text given.

6. ansibeautifier.Beautifier.reverse()

It returns like highlighted text.

``` Python
from ansibeautifier import Beautifier
b = Beautifier()
print(b.reverse(text="Hello World", always=True))
print(b.reset_intensity())
```

7. ansibeautifier.Beautifier.conceal()

It returns hidden text and you can unhide it by the ansibeautifier.Beautifier.reset_intensity() function.

``` Python
import time
from ansibeautifier import Beautifier
b = Beautifier()
print("Hello World")
print(b.conceal(text="Hello World"))
print("Hello World")
time.sleep(0.5)
print(b.reset_intensity())
```

Try this!

# Thanks for reading

If you want the source code you can visit my GitHub page
https://github.com/BoughtData92730/ansibeautifier