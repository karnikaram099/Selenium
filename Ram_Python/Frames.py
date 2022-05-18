#write a program to print all the lines in a file


path =r'C:\Users\karni\PycharmProjects\Alpha_3\file Handling\sample.txt'
# with open(path) as file:
#     for line in file:
#         print(line)


#wap to count the number of lines present in a file
# c =0
# with open(path) as file:
#     for line in file:
#         c = c+1
#     print(c)

#wap to print line number and line


# with open(path) as file:
#     for index,item in enumerate(file,start=1):
#         print(index,item)

#wap to print no. of words in the given file


# with open(path) as file:
#
#     c = 0
#     for line in file:
#         l = line.split()
#         for i in l:
#             c = c+1
#             print(c,i)


#wap to print lines from the last of the file

# with open(path) as file:
#     for line in reversed(list(file)):
#          print(line)


#wap to count the no. of spaces in file

# with open(path) as file:
#     c = 0
#     for line in file:
#
#         # l = line.split()
#
#         # for i in line:
#
#         if line in ' ':
#
#             c = c+1
#             print(c)


##wap to count the number of words startingwith vowel
# with open(path) as file:
#     for line in file:
#         l = line.split()
#         c=0
#         for i in l:
#             if i[0] in "aeioAEIOU":
#                 c = c+1
#                 print(c,i)

# with open(path) as file:
#     d ={}
#     for line in file:
#         l = line.split()
#         for i in l:
#             d[i] =l.count(i)
#     print(d)

#wap to extract all the ip address
f_path =("C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt")
# with open(f_path) as file