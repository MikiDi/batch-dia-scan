import os.path

def generate_scan_command_for_position(scanner_name, position, target_file_path):
    return " ".join([
        "scanimage",
        f'--device-name="{scanner_name}"',
        "-l", "{:3.1f}".format(position.x),
        "-t", "{:3.1f}".format(position.y),
        "-x", "{:3.1f}".format(position.x_width),
        "-y", "{:3.1f}".format(position.y_width),
        "--resolution=1800",
        "--mode=Color",
        "--format=tiff",
        "--depth=16",
        '--source="Transparency Unit"',
        f'--output-file="{os.path.expanduser(target_file_path)}"',
    ])
