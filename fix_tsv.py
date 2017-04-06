import pandas as pd
import sys

if __name__ == "__main__":
    user_file = sys.stdin
    corrected_file = pd.read_csv(userfile, sep = '\t', encoding = 'latin-1', error_bad_lines = False)
    corrected_file.write_csv(userfile, sep = '\t', index = False, encoding = 'utf-8')