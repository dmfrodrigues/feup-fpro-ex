def file_finder(dirs, file_name):
    if type(dirs) == str:
        if file_name == dirs:
            return file_name;
        else:
            return;

    for i in range(1, len(dirs)):
        s = file_finder(dirs[i], file_name);
        if s != None:
            return dirs[0] + '/' + s;
    return;

dirs = ["home",\
          ["Documents",\
             [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],\
             [ "Python", "hello_world.py", "readme.md" ],\
          ],\
          ["Downloads",\
             [ "Movies",\
                [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],\
                "1.avi", "22", "001.mp4"\
             ],\
          ],\
          "tmp.txt", "page.html"\
        ];

print(file_finder(dirs, 'Documents'))
print(file_finder(dirs, 'recursion.pdf'))