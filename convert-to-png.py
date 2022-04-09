import os
import subprocess

# Convert all svg files to png

# Changes the export resolution
dpi = 150

# Set True to print all executed commands
debug = False

inputDir = 'svg/'
outputDir = 'png/'
inkscape_path = '"C:/Program Files/Inkscape/bin/inkscape.exe" '
action_to_png = f'--export-area-drawing --export-dpi={dpi} '


def convert_to_png():
    files = os.listdir(inputDir)
    for file in files:
        if file.lower().endswith(".svg"):
            input_file = '"' + inputDir + file + '"'
            exp_file = outputDir + file.removesuffix("svg") + 'png" '
            export_file_param = '--export-filename="' + exp_file
            command = inkscape_path + export_file_param + action_to_png + input_file
            if debug:
                print(command)
            subprocess.call(command)
            print("Generated: " + exp_file)


if __name__ == '__main__':
    print("Start converting...")
    convert_to_png()
    print("Finish convert to png")
