class ScanMountPosition():
    """docstring for ScanMountPosition."""

    def __init__(self, l, t, x, y):
        super().__init__()
        self.x = l # Top-left x (in mm)
        self.y = t # Top-left y (in mm)
        self.x_width = x
        self.y_width = y

class ScanMount():
    """docstring for ScanMount."""

    def __init__(self, x_origin, y_origin, frame_width, frame_height,
                 n_frames_x, n_frames_y, inter_dist_x, inter_dist_y):
        super().__init__()
        self.x_origin = x_origin
        self.y_origin = y_origin
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.n_frames_x = n_frames_x
        self.n_frames_y = n_frames_y
        self.inter_dist_x = inter_dist_x
        self.inter_dist_y = inter_dist_y

    def generate_scan_mount_positions(self):
        positions = []
        for n_y in range(self.n_frames_y ):
            for n_x in range(self.n_frames_x):
                l = self.x_origin + n_x * self.inter_dist_x
                t = self.y_origin + n_y * self.inter_dist_y
                pos = ScanMountPosition(l, t, self.frame_width, self.frame_height)
                positions.append(pos)
        return positions
