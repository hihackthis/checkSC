# checkSC
Fast search for the code number on the **ShellCheck Wiki** pages. :flashlight:

[ShellCheck](https://github.com/koalaman/shellcheck) is a tool that provides warnings and suggestions for bash/sh shell scripts, as a way to search Wiki pages quickly, I wrote this program to make debugging more agile and efficient.

Note, there are two checkSC.py:

> checkSC_net.py, this will perform a search on the [ShellCheck Wiki](https://www.shellcheck.net/wiki) website.


> checkSC_gist.py, this will perform a search on the [GitHub Gist Wiki](https://gist.github.com/nicerobot/53cee11ee0abbdc997661e65b348f375) website.

## Usage
```
git clone https://github.com/hihackthis/checkSC.git
cd checkSC
pip install -r requeriments.txt
python checkSC.py
```
After that, you can be your search for the code number. Remember, you must add 'SC' first and numbers after. For example: SC1000

Let's see how easy is!

Run checkSC.py:

![](https://github.com/hihackthis/checkSC/blob/main/img/sc00.png)

So enter your code number SC:

![](https://github.com/hihackthis/checkSC/blob/main/img/sc01.png)

The default browser opens a new window with the code number:

![](https://github.com/hihackthis/checkSC/blob/main/img/sc02.png)

To search again close the browser and hit 'Y' or 'y' and enter your code number:

![](https://github.com/hihackthis/checkSC/blob/main/img/sc03.png)

If the code number doesn't exist, the checkSC will warn you. Finally, to exit the program press ENTER.

![](https://github.com/hihackthis/checkSC/blob/main/img/sc04.png)

## Final words 

Have fun! :sunglasses:
