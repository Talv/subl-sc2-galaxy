# subl-sc-galaxy
It's a plugin for Sublime Text editor (tested on Build 3083) that introduces support for *SC2 Galaxy Script* language.

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

## How to use this plugin in combo with SC2 Editor?
To avoid copy-pasting code from the sublime to trigger editor, or manually reimporting files after every change, you must save your map in an unpacked format - that is *.SC2Component* in save dialog.  
This way you will be able to open your map's directory in sublime. And write galaxy files directly through the filesystem.  
Thanks to this SC2 Editor will read your script files on demand - always up to date.

It's also recommended to not write your code directly into `MapScript.galaxy` as it might be easly overriden by editor. The better way is to create a custom block in trigger editor and include your custom scripts from there. This way:

![trigger editor](https://cloud.githubusercontent.com/assets/6976458/11614705/a03daefa-9c4a-11e5-95de-9b2bd1780dec.png)

Then create a file `scripts/bootstrap.galaxy`:

```
// scripts/bootstrap.galaxy

// here you might insert sub includes
// include "scripts/foo.galaxy"

bool onInit(bool testConds, bool runActions) {
    UIDisplayMessage(PlayerGroupActive(), c_messageAreaSubtitle, StringToText("HELLO WORLD"));
    return true;
}

void bootstrap() {
    // this is your entry point
    TriggerAddEventMapInit(TriggerCreate("onInit"));
}
```