import os
import collections

SearchResults = collections.namedtuple('SearchResult', 'file, line, text')


def print_header():
    print('-------------------------------------------------')
    print('              FILE SEARCHER')
    print('-------------------------------------------------')


def get_folder_from_user():
    folder = input("What folder do you want to search? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_text_from_user():
    text = input("What are you searching for [single phrases only]? ")
    return text.lower()


def search_file(filename, search_text):

    #matches = []

    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(line=line_num, file=filename, text=line)
                yield m
                #matches.append(m)

        #return matches



def search_folders(folder, text):
    #print('Would search {} for {}'.format(folder, text))

    #all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            #matches = search_folders(full_item, text)
            #all_matches.extend(matches)
            # for m in matches:
            #     yield m
            yield from search_folders(full_item, text)
        else:
            if  item.endswith('.txt'):
                yield from search_file(full_item, text)
            #matches = search_file(full_item, text)
            #all_matches.extend(matches)
            # for m in matches:
            #     yield m

    #return all_matches


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print(' Sorry we need a folder chief')
        return
    text = get_text_from_user()
    if not text:
        print(' Sorry we need to search some text')
        return
    
    matches = search_folders(folder,text)
    match_count = 0

    for m in matches:
        match_count += 1
        #print(m)
        print('--------------MATCH--------------')
        print('file: ' + m.file)
        print('line: {:,}'.format(m.line))
        print('match: ' + m.text.strip())
        print()

    print("Found {:,} matches.".format(match_count))




if __name__ == '__main__':
    main()