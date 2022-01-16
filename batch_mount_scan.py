import os
import re
from operator import itemgetter
import sys
import subprocess
from mount_scan.scanimage import generate_scan_command_for_position
from mount_scan.scan_mount import ScanMount

# https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts
def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=itemgetter(key), reverse=reverse)
    return xs

class BatchMountScanner():
    """Util class for managing file naming when batch scanning from a (slide-)mount"""

    FILENAME_FORMAT_STRING = "mount_{:02d}_frame_{:02d}.{}"
    FILENAME_REGEX = re.compile(r"mount_(?P<mount_index>\d{2})_frame_(?P<frame_index>\d{2})\.*")

    def __init__(self, target_folder):
        super()
        self.target_folder = target_folder
        self.ensure_target_folder()

    def ensure_target_folder(self):
        os.makedirs(self.target_folder, exist_ok=True)

    def parse_current_mount_frame_index(self):
        listing = os.listdir(self.target_folder)
        matches = [ BatchMountScanner.FILENAME_REGEX.match(s).groupdict() for s in listing ]
        if matches:
            parsed_matches = [{"mount_index": int(m["mount_index"]), "frame_index": int(m["frame_index"])} for m in matches]
            s_matches = multisort(parsed_matches, (("mount_index", False), ("frame_index", False)))
            return s_matches[-1]
        return None

    def next_mount_index(self):
        indexes = self.parse_current_mount_frame_index()
        if indexes:
            return indexes["mount_index"] + 1
        return 1

    def next_frame_path(self, mount_index, frame_index, extension="tiff"):
        fn = BatchMountScanner.FILENAME_FORMAT_STRING.format(mount_index, frame_index, extension)
        p = os.path.join(self.target_folder, fn)
        return p

# Specs for slide holder provided with Epson Perfection v850 Pro
SLIDE_WIDTH = 38.0
SLIDE_HEIGHT = 38.0
X_ORIGIN = 2.0
Y_ORIGIN = 32.0
INTER_DIST_X = 53.0
INTER_DIST_Y = 58.0

slide_mount = ScanMount(X_ORIGIN, Y_ORIGIN,
                  SLIDE_WIDTH, SLIDE_HEIGHT,
                  3, 4,
                  INTER_DIST_X, INTER_DIST_Y)

if __name__ == '__main__':
    # python3 batch_mount_scan.py "epson2:libusb:003:007" ~/test_folder
    scanner_name = sys.argv[1]
    target_folder_path = sys.argv[2]

    positions = slide_mount.generate_scan_mount_positions()
    
    scanner = BatchMountScanner(target_folder_path)
    mount_index = scanner.next_mount_index()
    for i in range(len(positions)):
        frame_path = scanner.next_frame_path(mount_index, i + 1)
        cmd = generate_scan_command_for_position(scanner_name, positions[i], frame_path)
        print(f"Scanning frame {i + 1} of {len(positions)} ...")
        proc_res = subprocess.run(cmd, check=True, shell=True)

    