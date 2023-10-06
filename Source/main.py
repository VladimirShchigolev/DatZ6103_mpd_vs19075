from Source.Museum import Museum


def main():
    with open("input.txt", "r") as fin:
        room_count, camera_pos_count, max_camera_count = [int(x) for x in fin.readline().strip().split()]
        camera_sights = []
        for camera in range(camera_pos_count):
            camera_sights.append([int(x) for x in fin.readline().strip().split()])

    museum = Museum(room_count, camera_pos_count, max_camera_count, camera_sights)
    solution = museum.LAHC()
    camera_positions = solution.to_position_array()
    print("cameras:", len(camera_positions))
    print("positions:", camera_positions)
    print("cost:", solution.cost())

    with open("output.txt", "w") as fout:
        print("cameras:", len(camera_positions), file=fout)
        print("positions:", camera_positions, file=fout)
        print("cost:", solution.cost(), file=fout)


if __name__ == "__main__":
    main()
