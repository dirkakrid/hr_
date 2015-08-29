hr 
====


Horizontal rule for your terminal with TASK NAME to be performed- in python!

Use the old `<hr />` tag, but in your terminal.

Check how much time you took to perform the mentioned task .


## Inspiration

             ##     "A problem well put, is half solved" -- John Dewey<hr/>
The original version can be found in  (https://github.com/LuRsT/hr).<br/>
It's elder brother can be found in (https://github.com/euangoddard/hr.py).

Add "TASK_NAME" in the horizontal rule, to keep you aware....


## Setup

    $ sudo pip install git+git://github.com/sumit007/hr_.git

## How to use it?

### From the command-line:

    $ hr
    ================================== Till the end of your terminal window
    $

    #Change the default symbol

    $ hr -s '*'
    ********************************** # Till the end of your terminal window
    $
    

### Mention the "task in written" which you want to intend to perform
    
    $hr -n "Task name" 
    ========  Task name =============== 
    
    $hr -n "OpenShift and python" -s "#"
    ###### OpenShift in python########  #Till the end of your terminal window    
    
    
### Check how much time you took to finish the task.

    $hr -n "well stated problem. Start time: xx:xx"
    =======  well stated problem. Start time: xx:xx  =========

## Requirements

The only requirement is python (tested in python 2.7)

##I know it's a small project, but still provide your feedback. They're are really valuable for me to improve
