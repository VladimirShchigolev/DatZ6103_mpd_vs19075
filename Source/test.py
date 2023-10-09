from Source.Museum import Museum


def main():
    for test_no in range(10):
        run_test(test_no+1)


def run_test(test_no):
    print("Test #"+str(test_no))

    with open("../Tests/test_"+str(test_no)+".txt", "r") as fin:
        room_count, camera_pos_count, max_camera_count = [int(x) for x in fin.readline().strip().split()]
        camera_sights = []
        for camera in range(camera_pos_count):
            camera_sights.append([int(x) for x in fin.readline().strip().split()])

    if camera_pos_count <= 30:
        time_limit = 3
    else:
        time_limit = camera_pos_count/10

    museum = Museum(room_count, camera_pos_count, max_camera_count, camera_sights)
    print("Solving LAHC...")
    solution_LAHC = museum.LAHC(time_limit=time_limit)
    camera_positions_LAHC = solution_LAHC.to_position_array()
    print("Done.")

    if museum.camera_position_count <= 30:
        print("Solving naive...")
        solution_naive, time_naive = museum.naive()
        camera_positions_naive = solution_naive.to_position_array()
        print("Done.")
    else:
        print("Skipping naive.")

    with open("../Tests/test_"+str(test_no)+"_out.txt", "w") as fout:
        print("Rooms:", museum.room_count, file=fout)
        print("Camera positions:", museum.camera_position_count, file=fout)
        print("Max number of cameras:", museum.max_camera_count, file=fout)
        print("Avg rooms per camera position:",
              round(sum([len(x) for x in museum.camera_sights])/museum.camera_position_count, 2),
              file=fout)
        print("\n" + "="*20 + "\n", file=fout)

        print("LAHC", file=fout)
        print("Cameras:", len(camera_positions_LAHC), file=fout)
        print("Positions:", camera_positions_LAHC, file=fout)
        print("Unsupervised rooms:", solution_LAHC.cost() // (museum.max_camera_count + 1),
              file=fout)
        print("Cost:", solution_LAHC.cost(), file=fout)
        print("Time spent:", time_limit, "s", file=fout)

        print("\n" + "=" * 20 + "\n", file=fout)

        print("Naive (Optimal solution)", file=fout)

        if museum.camera_position_count <= 30:
            print("Cameras:", len(camera_positions_naive), file=fout)
            print("Positions:", camera_positions_naive, file=fout)
            print("Unsupervised rooms:", solution_naive.cost() // (museum.max_camera_count + 1),
                  file=fout)
            print("Cost:", solution_naive.cost(), file=fout)
            print("Time spent:", round(time_naive, 2), "s", file=fout)
        else:
            print("Not Available", file=fout)


if __name__ == "__main__":
    main()
