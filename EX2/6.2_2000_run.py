import time


def timer(f, *arguments):
    start_time = time.time()
    map(f, arguments)
    end_time = time.time()
    dif_time = end_time - start_time
    print("the time of the function execution is: ", dif_time)


def main():
    timer(lambda x: x+[1], [1, 2, 3], [4, 5, 6])
    name = "bug"
    timer("hi {name}".format, name)


if __name__ == '__main__':
    main()
