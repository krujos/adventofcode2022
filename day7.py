class Directory:

    def __init__(self, name, parent):
        self.size = 0
        self.parent = parent
        self.children = list()
        self.name = name

def is_command(buffer):
    return buffer[0] == '$'

def get_root(dir):
    if dir.parent is None:
        return dir
    return get_root(dir.parent)

def cd(line, curdir):
    dir_name = line[4:].strip()
    if dir_name == "..":
        if curdir.parent is not None:
            return curdir.parent
        return curdir

    if dir_name == "/":
        return get_root(curdir)

    for c in curdir.children:
        if c.name == dir_name:
            return c

    d = Directory(name=dir_name, parent=curdir)
    curdir.children.append(d)

    return d


def set_size(buffer, idx, curdir):
    dir_size = 0
    index=idx+1

    while not is_command(buffer[index]):
        s = buffer[index].split()[0]
        if s.isnumeric():
            dir_size +=int(s)
        index+=1
        if index >= len(buffer):
            break
    d = curdir
    #add this size to all the parent sizes
    while d is not None:
        d.size += dir_size
        d = d.parent


def get_size_under(d, under, dirs):
    if dirs is None:
        dirs = list()

    if d.size <= under:
        dirs.append(d.size)

    for c in d.children:
        get_size_under(c, under, dirs)

    return dirs

def run():
    root = Directory(name="/", parent=None)
    curdir = root
    with open('input_day7.txt') as f:
        b = f.read().splitlines()
    f.close()

    for i, v in enumerate(b):
        if v.startswith('$ cd'):
            curdir = cd(v, curdir)
        if v.startswith('$ ls'):
            set_size(b, i, curdir)

    small_dirs = get_size_under(root, 100000, None)
    print(sum(small_dirs))

if __name__ == '__main__':
  run()