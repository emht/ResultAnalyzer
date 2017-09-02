# Usage: ./read_argv.py --[min/max/mean] [filenames]
import sys
import numpy as np

def main():
    # Storing the name of script called
    script = sys.argv[0]

    # Store the action demanded by the user with the script
    action = sys.argv[1]

    # Store the filenames called with the script
    for filename in sys.argv[2:]:
        data = np.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = np.min(data, axis=1)
        elif action == '--mean':
            values = np.mean(data, axis=1)
        elif action == '--max':
            values = np.max(data, axis=1)
        
        for m in values:
            print(m)

if __name__ == "__main__":
    main()