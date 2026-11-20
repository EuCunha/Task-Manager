from argparse import ArgumentParser, Namespace

def cli():
    parser = ArgumentParser(
        prog="Task Manager",
        description="A simple app for you to stay in control of your daily tasks.",
        epilog="Example: py main.py -t 'First task' --add")

    parser.add_argument('-t', '--task', help="Takes task text and waits for flags, if none given, it echos the text.")
    parser.add_argument('-a', '-add', help="Append given task database.")
    parser.add_argument('-r', '-remove', help="Remove given task (by its position) from file.")
    parser.add_argument('-l', '--list', help="List all current tasks in the database")

    args: Namespace = parser.parse_args()

if __name__ == "__main__":
    cli()