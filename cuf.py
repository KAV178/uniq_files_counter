from os import listdir, path
from re import findall as fa
from datetime import datetime as dt
import sys
valid_files, trash_files = 0, 0


def print_progress(iteration, total, prefix ='', suffix ='', decimals = 2, barLength = 100):
    filled_length = int(round(barLength * iteration / float(total)))
    percents = round(100.00 * (iteration / float(total)), decimals)
    bar = '#' * filled_length + '-' * (barLength - filled_length)
    sys.stdout.write('\r%s [%s] %s%s %s' % (prefix, bar, percents, '%', suffix)),
    sys.stdout.flush()
    if iteration == total:
        print("\n")


def get_ufc(dir_name):
    global valid_files, trash_files
    result = {}

    f_lst = listdir(dir_name)
    f, f_cnt = 0, len(f_lst)
    print_progress(f, f_cnt, prefix='Progress:', suffix='Complete', barLength=50)
    for f_name in f_lst:
        f += 1
        print_progress(f, f_cnt, prefix='Progress:', suffix='Complete', barLength=50)
        if path.isfile(path.join(dir_name, f_name)):
            cl_f_name = fa(r'([\w_]+)_1-', f_name)
            if len(cl_f_name) > 0:
                valid_files += 1
                result[cl_f_name[0]] = result[cl_f_name[0]] + 1 if cl_f_name[0] in result.keys() else 1
            else:
                trash_files += 1
    return result


start_ts = dt.now()
data = get_ufc(sys.argv[1])
if len(data) > 0:
    print("{0:50}|{1:15}".format("File name group",  " "*10+"Count"))
    print("{0:50}+{1:15}".format("-"*50,  "-"*15))
    for k, v in data.items():
        print("{0:50}|{1:15}".format(k,  v))
    print("{0:50}+{1:15}".format("-" * 50, "-" * 15))
    print("{0:50}|{1:15}".format("Total valid name groups:", len(data)))
    print("{0:50}|{1:15}".format("Total valid files:", valid_files))
    print("{0:50}|{1:15}".format("Total trash files:", trash_files))
print("\nTime spent: {0}".format(dt.now() - start_ts))

