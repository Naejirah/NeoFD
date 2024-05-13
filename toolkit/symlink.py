from pyuac import main_requires_admin
from os import symlink
import argparse

@main_requires_admin(return_output=True)
def main():
    parser = argparse.ArgumentParser(description='Lancement de symlink', usage="""
        symlink.py -src <src> -dest <dest>  """)

    # Positional arguments
    # parser.add_argument('command', choices=['launch'],
    #                     help='Specify the command')
    
    launch_group = parser.add_argument_group('Launch Options',
                                               argument_default=argparse.SUPPRESS)
    launch_group.add_argument('-src', type=str, default="IA/falcon/models/falcon-7b", dest='src',
                                help='Chemin de source')
    launch_group.add_argument('-dest', type=str, dest='dest',
                                help='Chemin de sortie')
    
    args = parser.parse_args()

    print(args.src, args.dest)

    symlink(args.src, args.dest)

if __name__ == "__main__":
    rv = main()
    if not rv:
        print("I must have already been Admin!")
    else:
        admin_stdout_str, admin_stderr_str, *_ = rv