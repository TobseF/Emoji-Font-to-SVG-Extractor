import os
import subprocess

from typing import List, TextIO

# Reads a font and generates an SVG file for every emoji

outDir = "svg/"

# UTF8 encoded table which all Unicode symbols
# Header: Symbol;Hex-Code;Name;Is-Emoji (0 | 1);Group
# Example: 👍;1F44D;THUMBS UP SIGN;1;Body;
# Only symbols which are marked with Is-Emoji (1) are processed.
symbol_table = "symbol-table.csv"

# Simple SVG-Template with one centered symbol.
symbol_template = "symbol-template.svg"

# Simple SVG-Template with one centered symbol.
font = "Segoe UI Emoji"

inkscape_path = '"C:/Program Files/Inkscape/bin/inkscape.exe" '
action_object_to_path = '--export-overwrite --actions="select-by-id:text-box; object-to-path; export-id:text-box; '
action_export = 'export-id:text-box; export-do; FileClose" '

# Set True to print all executed commands
debug = False

# Writes a unicode emoji as svg into the $outDir.
def write_new_letter(glyph, hex_code, decimal, name, category):
    # the actual text file name
    letter_template: TextIO = open(symbol_template, "r")

    template_letter = "A"
    file_name = outDir + category + " - " + str(decimal) + " (" + name.lower() + ").svg"
    new_letter = open(file_name, "x", encoding='utf-8')

    lines: list[str] = letter_template.readlines()

    export_data = []
    for line in lines:
        export_data += line \
            .replace(">" + template_letter + "<", ">" + glyph + "<") \
            .replace("Arial", font)

    new_letter.writelines(export_data)
    new_letter.close()
    convert_to_path(file_name)


def convert_to_path(file_name):
    input_file = '"' + file_name + '"'
    command = inkscape_path + action_object_to_path + action_export + input_file
    if debug:
        print(command)
    subprocess.call(command)
    print("New symbol: " + input_file)


# Reads all Unicode-Emoji which are listed in the $symbol_table.
# Only symbols which are marked with Is-Emoji (1) are processed.
def generate_symbols():
    emoji_list = open(symbol_table, "r", encoding='utf-8')
    i = 0
    for line in emoji_list:
        i = i + 1
        values = line.split(";")
        glyph = values[0]
        hex_code = values[1]
        decimal = int(hex_code, 16)
        name = values[2]
        is_emoji = values[3] == "1"
        category = values[4]
        if is_emoji:
            write_new_letter(glyph, hex_code, decimal, name, category)


if __name__ == '__main__':
    print("Exporting all emoji...")
    generate_symbols()
    print("Finished export")
