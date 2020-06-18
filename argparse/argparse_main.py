"""Python argparse sample codes
"""
import argparse
import sys


def define_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Sample argparse")

    parser.add_argument("-i", "--id", help="Type your id", action="store")
    parser.add_argument("-o", "--on", help="Set Enable", action="store_true")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--input_csv", help="Input csv file", action="store")
    group.add_argument("-j", "--input_json", help="Input json file", action="store")

    parser.add_argument(
        "-r", "--retry", help="Repeat result", action="count", default=0
    )
    parser.add_argument("scores", nargs="*", help="Type Target names", type=int)

    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

    return args


def main():
    args = define_args()

    user_id = args.id
    status = "active" if args.on else "deactivated"

    input_file_type = "none"
    input_file = "none"
    if args.input_csv:
        input_file_type = "csv"
        input_file = args.input_csv
    elif args.input_json:
        input_file_type = "json"
        input_file = args.input_json

    scores = args.scores
    retry_count = args.retry if args.retry > 0 else 1

    for _ in range(retry_count):
        print("-" * 30)
        print(
            f"user_id:{user_id}, status:{status}, file type:{input_file_type}, file:{input_file}"
        )
        for num, score in enumerate(scores, start=1):
            print(f"{num} score: {score}")
        print(f"sum={sum(scores)}")


if __name__ == "__main__":
    main()
