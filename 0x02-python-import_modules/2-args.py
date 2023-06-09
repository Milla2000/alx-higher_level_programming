import sys

args = sys.argv[1:]  # Exclude the script name from the arguments

num_args = len(args)

if num_args == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
