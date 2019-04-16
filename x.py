import csv
import os

#change path to responses below
filename = os.path.join("/Users", "injuredroman", "Downloads", "g16_responses.csv")

csv_file = csv.reader(open(filename), delimiter=",")
i = 0
collated_results = dict()
section_name = "presentation_WTP"
collated_results[section_name] = dict()
section_name = "annotation_WTP"
collated_results[section_name] = dict()
for row in csv_file:
    if (i == 0):
        col_names = row
        i += 1
        continue
    ### logic to determine willing to pay for presentations
    start = 5
    end = 10

    relevant_answers = row[start:end]
    section_name = "presentation_WTP"

    cur_WTP = 215
    for j in range(len(relevant_answers)):
        next_answer = relevant_answers[j]
        if "chalkboard" in next_answer.lower():## case in which they've passed limit of WTP
            total_WTP = cur_WTP + 15*(j+1)

            collated_results[section_name][total_WTP] = collated_results[section_name].get(total_WTP, 0) + 1 # counting occurences of each
            break

    ### logic to determine willing to pay for annotations
    start = 10
    # end = 10
    relevant_answers = row[start:]
    section_name = "annotation_WTP"

    cur_WTP = 215
    for k in range(len(relevant_answers)):
        next_answer = relevant_answers[k]
        # print('chalkboard' in next_answer.lower())
        if "chalkboard" in next_answer.lower():## case in which they've passed limit of WTP
            total_WTP = cur_WTP + 15*(k+1)
            collated_results[section_name][total_WTP] = collated_results[section_name].get(total_WTP, 0) + 1 # counting occurences of each
            break

    i += 1

print(collated_results)

for s in collated_results:
    running_sum = 0; running_count=0;
    for wtp in collated_results[s]:
        running_sum += wtp * collated_results[s][wtp]
        running_count += collated_results[s][wtp]
    print("{}: ${}".format(s, running_sum/running_count))

