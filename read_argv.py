# Usage: ./read_argv.py --[min/max/mean] [filenames]
import sys
import numpy as np

def main():
    # Storing the name of script called
    script = sys.argv[0]

    # Store the action demanded by the user with the script
    action = sys.argv[1]

    # Store the filenames called with the script
    filenames = sys.argv[2:]

    # Checking if the inputted is action is permitted or not
    assert action in ['--min', '--min', '--max'], \
            'Action is not permitted, ,try --[mean/min/max]' + action
    
    # Process the file if the action is correct
    for file in filenames:
        process(file, action)

# Defining the process
def process (filename, action):
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