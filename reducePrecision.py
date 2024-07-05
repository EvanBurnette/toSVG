#!python3

import re
import sys
import os

def reduce_precision(svg_content, precision):
    def round_match(match):
        return f"{float(match.group()):.{precision}f}"
    
    # Regex to find floating point numbers excluding 1.0
    number_regex = re.compile(r"\d+\.\d+")
    
    # Substitute numbers with reduced precision
    new_svg_content = number_regex.sub(round_match, svg_content)
    if (precision == 0):
      version_regex = re.compile(r'version="1"')
      new_svg_content = version_regex.sub('version="1.0"', new_svg_content)

    return new_svg_content

def generate_output_path(input_svg_path):
    base, ext = os.path.splitext(input_svg_path)
    return f"{base}_smol{ext}"

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_svg_path> <precision>")
        sys.exit(1)
    
    input_svg_path = sys.argv[1]
    precision = int(sys.argv[2])
    output_svg_path = generate_output_path(input_svg_path)

    try:
        with open(input_svg_path, 'r') as file:
            svg_content = file.read()
    except FileNotFoundError:
        print(f"Error: File {input_svg_path} not found.")
        sys.exit(1)
    
    new_svg_content = reduce_precision(svg_content, precision)
    
    with open(output_svg_path, 'w') as file:
        file.write(new_svg_content)
    
    print(f"SVG file with reduced precision saved as {output_svg_path}")

if __name__ == "__main__":
    main()
