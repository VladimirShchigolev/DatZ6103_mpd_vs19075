from copy import copy
from random import randint


class CameraArrangement:
    def __init__(self, museum, camera_arrangement):
        self.museum = museum
        self.camera_arrangement = camera_arrangement

    def generate_next_arrangement(self):
        camera = randint(0, self.museum.camera_position_count-1)
        new_arrangement = copy(self.camera_arrangement)
        new_arrangement[camera] = not new_arrangement[camera]
        return CameraArrangement(self.museum, new_arrangement)

    def cost(self):
        arrangement_cost = 0

        # cost from uncovered rooms:
        for room in range(self.museum.room_count):
            cameras = 0
            for camera_pos in self.museum.room_camera_positions[room]:
                if self.camera_arrangement[camera_pos]:
                    cameras += 1

            arrangement_cost += max(2-cameras, 0)

        # give cost priority to unsupervised rooms
        arrangement_cost *= (self.museum.max_camera_count+1)

        # cost from used cameras
        used_cameras = sum(self.camera_arrangement)
        if used_cameras <= self.museum.max_camera_count:
            arrangement_cost += used_cameras
        else:
            arrangement_cost = self.museum.room_count*2*(self.museum.max_camera_count+2)  # basically +infinity

        return arrangement_cost

    def to_position_array(self):
        res = []
        for camera in range(len(self.camera_arrangement)):
            if self.camera_arrangement[camera]:
                res.append(camera)

        return res
