import time

from Source.CameraArrangement import CameraArrangement


class Museum:

    def __init__(self, room_count, camera_position_count, max_camera_count, camera_sights):
        self.room_count = room_count
        self.camera_position_count = camera_position_count
        self.max_camera_count = max_camera_count
        self.camera_sights = camera_sights

        self.room_camera_positions = [list() for room in range(room_count)]
        for camera_position in range(len(camera_sights)):
            for room in camera_sights[camera_position]:
                self.room_camera_positions[room].append(camera_position)

    def LAHC(self, n=1000, time_limit=2):
        best_solution = solution = CameraArrangement(self, [False for camera in range(self.camera_position_count)])
        best_cost = solution_cost = solution.cost()
        late_acceptance = [best_cost for k in range(n)]
        k = 0

        start_time = time.time()
        while time.time() - start_time < time_limit:
            candidate = solution.generate_next_arrangement()
            candidate_cost = candidate.cost()

            if candidate_cost < best_cost:
                best_solution = candidate
                best_cost = candidate_cost

            if candidate_cost < solution_cost or candidate_cost < late_acceptance[k]:
                solution = candidate
                solution_cost = candidate_cost

            late_acceptance[k] = candidate_cost
            k = (k+1) % n

        return best_solution

    def naive(self):
        subset_count = 2**self.camera_position_count
        best_solution = CameraArrangement(self, [False for camera in range(self.camera_position_count)])
        best_cost = best_solution.cost()

        time_start = time.time()

        for subset_id in range(subset_count):
            subset = [bool(subset_id & (1 << bit)) for bit in range(self.camera_position_count)]
            solution = CameraArrangement(self, subset)
            solution_cost = solution.cost()

            if solution_cost < best_cost:
                best_cost = solution_cost
                best_solution = solution

        return best_solution, time.time()-time_start
