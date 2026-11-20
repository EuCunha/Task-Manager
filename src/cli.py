from argparse import ArgumentParser, Namespace

# HANDLERS - ADD | DEL | VIEW
# TODO: Implement file parameter and set comunication with operations.py
def handle_add(argument: Namespace, array: list):
    return array.append(argument)

def handle_delete():
    pass

def handle_view(argument: str, array: list):
    if argument and argument.isdigit():
        print(f'{argument}. {array[int(argument) - 1]}')
    else:
        for i,task in enumerate(array, 1):
            print(f'{i}. {task}')

# PARSER BULDER
def build_parser():
    parser = ArgumentParser(
        prog='Task test',
        description='A simple task manager test',
        epilog='python <filename>.py add "<task>"'
    )
    subparser = parser.add_subparsers(
        title='Edit tasks list',
        dest='cmd',
        # required=True,
    )
    create = subparser.add_parser(
        name='create',
        aliases=['add'],
        help='Creates and add task to the database.',
        epilog='Example: py <filename>.py add "task"'
    )
    create.add_argument('task', help='Description of the task to be created.')

    remove = subparser.add_parser(
        name='remove',
        aliases=['del','rm'],
        help='Delete selected task from the database.',
        epilog='Example: py <filename>.py del ("task" or Index)'
    )
    remove.add_argument('task', help='Description of the task to be deleted.')
    
    view = subparser.add_parser(
        name='list',
        aliases=['view'],
        help='Display all the tasks (if no parameter given).',
        epilog='Example: py <filename>.py list (index)'
    )
    view.add_argument('-i','--index', help='Index of the task to be displayed.')

    subparser.add_parser(
        name='clear',
        help='Clear current list.',
        epilog='Example: py <filename>.py clear'
    )
    
    return parser.parse_args()

# MAIN PARSER LOOP
# Implement the connection with the Task Manager Main file
def run(array: list): 
    args: Namespace = build_parser()
    print(args)

    if args.cmd:
        if args.cmd in ('add', 'create'):
            handle_add(args.task, array)
        if args.cmd in ('remove', 'del', 'rm'):
            pass
        if args.cmd in ('list', 'view'):
            handle_view(args.index, array)
        if args.cmd in ('clear'):
            array.clear()


if __name__ == "__main__":
    test = [1,2,3,4,5]
    run(test)
    print(test)