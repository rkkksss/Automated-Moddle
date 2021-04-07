import os
import argparse
import shutil
import re


parser = argparse.ArgumentParser(description='Раскладываем фоточки')
parser.add_argument('--dest', metavar='DIR', type=str, required=True,
                    help='dir for result')
parser.add_argument('--pic-path', metavar='DIR', type=str, required=True,
                    help='dir with pictures')
parser.add_argument('--text-path', metavar='DIR', type=str, required=True,
                    help='dir with text')
parser.add_argument('--force', action='store_true',
                    help='delete destination directory if exists')

args = parser.parse_args()

if args.force:
    shutil.rmtree(args.dest)
elif os.path.exists(args.dest):
    print(f'Dir "{args.dest}" already exists')
    exit()

if not os.path.exists(args.pic_path):
    print(f'Dir "{args.pic_path}" doesn\'t exist')

if not os.path.exists(args.text_path):
    print(f'Dir "{args.text_path}" doesn\'t exist')

os.mkdir(args.dest)

def dir_name(i):
    return f'{args.dest}/test {i}'


def create_dir(i):
    name = dir_name(i)
    if not os.path.exists(name):
        os.mkdir(name)
    return name


def test_index(test_name):
    txt = re.match('Задание №(\d+)', test_name).group(1)
    return txt


def pic_index(pic_name):
    txt = re.match('задание(\d+)', pic_name).group(1)
    return txt

print('Copying text files...')

test_dir = args.text_path
for dirpath, dirnames, filenames in os.walk(test_dir):
    for file in filenames:
        i = test_index(file)
        dst = create_dir(i)
        shutil.copy(f'{test_dir}/{file}', dst)

print('Copying pictures...')

pic_dir = args.pic_path
for dirpath, dirnames, filenames in os.walk(pic_dir):
    for file in filenames:
        i = pic_index(file)
        dst = create_dir(i)
        shutil.copy(f'{pic_dir}/{file}', dst)

print('Making archives...')

dirpath, dirnames, filenames = next(os.walk(args.dest))

for dir in dirnames:
    shutil.make_archive(f'{args.dest}/{dir}', 'zip', f'{args.dest}/{dir}')

print('Done!')
