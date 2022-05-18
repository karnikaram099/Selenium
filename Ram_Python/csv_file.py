import csv
# path = r"C:\Users\Vidya\PycharmProjects\Alpha_3_batch\files_directory\csv_files\sample.csv"
with open("example csv_file", 'w') as csv_file:
    write = csv.writer(csv_file)
    write.writerow("Ram is a mechanical student")