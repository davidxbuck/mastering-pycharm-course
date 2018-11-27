import service


def main():
    print_welcome()

    service.download_info()

    for show_id in range(100, 141):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def print_welcome():
    print("Welcome")
    print()


if __name__ == '__main__':
    main()


