# 😁 🔀 Font emoji to SVG / PNG Extractor
> 💡 Extracts svg or png files for every font symbol. Simple letters will be skipped.

This Python script reads an installed system font and converts every symbol to an SVG file.  
Optional, all SVG files can be converted to PNG. It uses the 
[Inkscape CLI](https://wiki.inkscape.org/wiki/index.php/Using_the_Command_Line) for conversion.  
The selection of symbols can be configured with the `symbol-table.csv`. It's configured to only
export colorful symbols.

## ⭐ Features
 ⭐ Batch Processing of all emoji  
 ⭐ Convert to SVG or PNG  
 ⭐ Grouping by category (Animals, Food, Objects)  
 ⭐ Cuts of empty space  
 ⭐ Tested on Windows


## 🛠 Setup
 * Install [Inkscape](https://inkscape.org) version 1.0 or later.
 * Install [Python](https://inkscape.org) version 3.6 or later.
 * Configure `inkscape_path` in the script.


## 🚀 Run
To export all emoji svg run:
```shell
python export-all-emoji.py
```

To convert all exported svg file to png run:
```shell
python convert-to-png.py
```


## 🛠 Config
 * `inkscape_path`: Path to your Inkscape installation. 
 * `font`: Font to export. For example "_Segoe UI Emoji_".
 * `dpi`: Change the png resolution. 
 * `outDir`: Output directory.
 * `debug`: Enable to also print all console commands.
