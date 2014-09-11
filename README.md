hr
====


Horizontal rule for your terminal with TASK NAME to be performed- in python!


Use the old `<hr />` tag, but in your terminal.

## Inspiration
The original version can be found in  (https://github.com/LuRsT/hr).
It's elder brother can be found in (https://github.com/euangoddard/hr.py).

Added a feature: Add "TASK_NAME" in the horizontal rule, to keep you focussed on the task which you intended to perform.


## Setup

    $ pip install git+git://github.com/sumit007/hr_.git

## How to use it?

### From the command-line:

    $ hr
    ================================== Till the end of your terminal window
    $

    $ hr -s '*'
    ********************************** # Till the end of your terminal window
    $
    

### Mention the "task in written" which you want to intend to perform
    
    $ hr -n "Task name" 
    ========  Task name =============== 
    
    $hr -n "OpenShift and python" -s "#"
    ###### OpenShift in python########  #Till the end of your terminal window    

## Requirements

The only requirement is python (tested in python 2.7)
