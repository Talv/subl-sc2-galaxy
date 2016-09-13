# SC2 Galaxy script package for Sublime Text editor
Plugin for Sublime Text editor (tested on Build 3083) that introduces support for *SC2 Galaxy Script* language.

## Installation

### Linter installation

Requires [SublimeLinter](http://www.sublimelinter.com/en/latest/installation.html#installing-via-pc) package to be installed.

Before using this plugin, you must ensure that [nectan](https://github.com/Talv/nectan) is installed on your system. To install `nectan`, do the following:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `nectan` by typing the following in a terminal:
   ```
   [sudo] pip install https://github.com/Talv/nectan/archive/master.zip
   ```

### Plugin installation
Clone this repository into a subdirectory named `subl-sc2-galaxy` in a *Packages* directory of the sublime editor.  
```~/.config/sublime-text-3/Packages``` (Linux)  
```C:\Users\YOUR_NAME\AppData\Roaming\Sublime Text 3\Packages``` (Windows)
```
cd ~/.config/sublime-text-3/Packages
git clone https://github.com/Talv/subl-sc2-galaxy.git
```

## Configuration
Ensure that galaxylint is enabled by using command `Sublime Linter: Enable linter` (might be enabled by default).

## Features

### Syntax highlighting
![syntax highlighting](https://cloud.githubusercontent.com/assets/6976458/11614372/276ccbf4-9c41-11e5-8648-7f708e5df3fa.png)


### Code linter
Basic code linting - currently performs only syntax checking.
![syntax check](https://cloud.githubusercontent.com/assets/6976458/11614383/79b648fe-9c41-11e5-89b8-ca2becee2153.png)

### Completion of native functions
Native functions and constants are mapped into sublime-completions.
![natives completion](https://cloud.githubusercontent.com/assets/6976458/11614389/bba6f510-9c41-11e5-9d00-46ef7afa8ad6.png)
(will expand into `UnitGetFacing(unit inUnit)`)

### Snippets

 * `st` struct
 * `stref` structref
 * `tgs` trigger simple formatting
 * `tgc` trigger complex formatting
 * `for` for loop
 * `foru` for loop iterating units
 * `forp` for loop iterating players

## How to use this plugin in combination with SC2 Editor?
To avoid copy-pasting code from sublime to trigger editor, or manually reimporting .galaxy files after every change, you must save your map in an unpacked format - that is *.SC2Component* in save dialog.

This will expose your map files to be accessed through the filesystem. Take advantage of it and open your map's directory as sublime project.

Then you can just save your scripts directly into the map, without any additional importing in SC2 editor. Your scripts will be read on demand - always up to date.

It's also advised to not write your code directly into `MapScript.galaxy` as it might be easly overriden by sc2 editor. The better way is to create a custom script block in trigger editor and include your scripts from there. 

For Example:

![trigger editor](https://cloud.githubusercontent.com/assets/6976458/11614705/a03daefa-9c4a-11e5-95de-9b2bd1780dec.png)
* Note the Initialization Function (Optional) on bottom

Navigate into your MAPFILE.SC2Map directory and create a `scripts` directory. Inside it, create two files:
```c
// scripts/bootstrap.galaxy

// This is the primary bootstrap file. It will bootstrap main, among other required environment files needed.
include "scripts/main.galaxy"

void bootstrap() {
   //Comment out the below line after confirming it works.
	UIDisplayMessage(PlayerGroupActive(), c_messageAreaSubtitle, StringToText("Bootstrap"));
	main(); //Call main, it is suggested most internal systems should hook off main's initialization.
}
```

```c
// scripts/main.galaxy

// here you might insert sub includes, e.g.
//include "scripts/foo.galaxy"

bool onInit(bool testConds, bool runActions) {
    UIDisplayMessage(PlayerGroupActive(), c_messageAreaSubtitle, StringToText("HELLO WORLD"));
    return true;
}

void main() {
    // this is your entry point
    TriggerAddEventMapInit(TriggerCreate("onInit"));
}
```
