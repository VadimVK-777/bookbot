def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words1(path_to_file):
    file_contents = read_file(path_to_file)
    return len(file_contents.split())

def get_num_words(path_to_file):
    file_contents = read_file(path_to_file)
    print(f'{len(file_contents.split())} words found in the document')

def get_num_alpha(path_to_file):
    alpha_dict = {}
    file_contents = read_file(path_to_file).lower()
    for elem in file_contents:
        if elem.isalpha():
            if elem in alpha_dict:
                alpha_dict[elem] += 1
            else:
                alpha_dict[elem] = 1
    return alpha_dict

def my_report(path_to_file):
    alpha_list = []
    file_contents = get_num_alpha(path_to_file)
    for key,value in file_contents.items():
        alpha_list.append({'char': key, 'num': value})
    alpha_list.sort(reverse=True, key=lambda x: x['num'])
    return alpha_list

def print_report(path_to_file):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path_to_file}...')
    print('----------- Word Count ----------')
    print(f'Found {get_num_words1(path_to_file)} total words')
    print('--------- Character Count -------')
    alpha_list = my_report(path_to_file)
    for item in alpha_list:
        print(f'{item['char']}: {item['num']}')
    print('============= END ===============')


