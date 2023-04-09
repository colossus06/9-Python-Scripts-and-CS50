exams=list()


with open("articles_list.txt") as fin:
    for line in fin:
        exams.append(line)

exams.sort()
#print(articles)

new_file= "sorted_articles.txt"

with open (new_file, "w") as fout:
    for exam in exams:
        fout.write(exam)

