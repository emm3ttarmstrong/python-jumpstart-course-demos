import os
import platform
import subprocess
import cat_service


def main():
    # print header
    print_the_header()

    # get or create output folder
    folder = get_or_create_output_folder()
    print('Found or created folder: ' + folder)

    # download cats
    download_cats(folder)

    # display cats
    display_cats(folder)

def print_the_header():
    print('----------------------------------------')
    print('             LOLCAT FACTORY')
    print('----------------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path

def download_cats(folder):
    print('contacting server to download your cats...')
    cat_count = int(input('How many cats do you want? '))
    for i in range(1,cat_count+1):
        print('downloading cat {}...'.format(i))
        name = 'lolcat_{}'.format(i)
        cat_service.get_cat(folder, name)

def display_cats(folder):
    print('displaying cats folder...')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['start', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your operating system ({}).".format(platform.system()))


if __name__ == '__main__':
    main()