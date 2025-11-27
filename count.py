import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simple interactive counter. Press Enter to increment, q to quit."
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Starting value (default: 0)",
    )
    parser.add_argument(
        "--step",
        type=int,
        default=1,
        help="Increment step (default: 1)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Optional upper limit; stop when the count exceeds this value",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count = args.start
    step = args.step
    limit = args.limit

    def show_help() -> None:
        print("Interactive counter")
        print(
            "Enter: increment | q: quit | r: reset | -: decrement | "
            "set N: set value | step N: change step | h: help"
        )
        print()

    show_help()

    while True:
        print(f"count: {count}")
        command = input("> ").strip()

        if command == "":
            count += step
            if limit is not None and count > limit:
                print(f"Reached limit {limit}. Bye.")
                break
        elif command == "-":
            count -= step
        elif command.lower() == "q":
            print("Bye.")
            break
        elif command.lower() == "r":
            count = args.start
            step = args.step
        elif command.lower() in {"h", "help", "?"}:
            show_help()
        elif command.lower().startswith("set "):
            try:
                count = int(command.split(maxsplit=1)[1])
            except (IndexError, ValueError):
                print("Usage: set <integer>")
        elif command.lower().startswith("step "):
            try:
                step = int(command.split(maxsplit=1)[1])
            except (IndexError, ValueError):
                print("Usage: step <integer>")
        else:
            print("Unknown command. Use Enter, q, r, set N, or step N.")


if __name__ == "__main__":
    main()
