import os


def harry_chapters():
    """
    find and rename the correct number and name of each chapter
    :return:
    """
    directory = r'potter'

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Loop through each file and rename it
    for filename in files:
        new_name = ''
        with open(directory + '\\' + filename) as file:
            for i in range(9):
                x = file.readline()
                if 'Chapter' in x:
                    x = x.split("Chapter")
                    y = x[1].split(":")
                    new_name = str(int(y[0]))
                    new_name = new_name.zfill(3)
                    new_name += y[1].split("<")[0] + '.html'
                    print(new_name)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
