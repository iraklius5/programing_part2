from datetime import datetime
import re


def find_top5_successful_requests():
    pattern = re.compile(r"\"POST /cgi-bin/geturlstats\.pl HTTP/1\.0\" 200 \d+")
    date = '%d/%b/%Y:%H:%M:%S'
    date_from = datetime.strptime('3/Jul/1995:10:39:35', date)
    date_to = datetime.strptime('3/Jul/1995:11:59:29', date)
    counts = []
    with open('access_log_Jul95.txt', 'r') as file:
        for line in file.readlines():
            line_parts = line.split()

            if date_from < datetime.strptime(line_parts[3].lstrip('['), date) < date_to and line_parts[5] == "\"POST" \
                    and line_parts[8] == "200":
                counts.append(line_parts[9])
            if not (datetime.strptime(line_parts[3].lstrip('['), date) < date_to):
                break
    print(counts)
    dict_ = {}
    for x in counts:
        dict_[x] = counts.count(x)
        while x in counts:
            counts.remove(x)

    print(dict_)
    sort_orders = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    j = 0
    for i in sort_orders:
        print(f"Rank by popularity: {j + 1}\n", f"id of request:\"{i[0]}\"\n", f"Number of requests:{i[1]}\n\n")
        if j == 4:
            break
        else:
            j += 1


if __name__ == '__main__':
    find_top5_successful_requests()
