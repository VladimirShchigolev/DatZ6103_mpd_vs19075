import random


def main():
    random.seed(0)
    for test_no in range(10):
        if test_no < 5:
            M = (test_no+1) * 5
        else:
            M = (test_no+1) * 100
        N = random.randint(M//2, M*2)
        K = random.randint(M//2, M)

        density = random.uniform(2/N, 1/2)

        with open("../Tests/test_"+str(test_no+1)+".txt", 'w') as test:
            print(N, M, K, file=test)
            for camera_pos in range(M):
                rooms = []
                for room in range(N):
                    if random.random() < density:
                        rooms.append(room)
                print(*rooms, file=test)


if __name__ == "__main__":
    main()
