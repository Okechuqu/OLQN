import csv


def write_rows(response, rows):
    writer = csv.writer(response)
    writer.writerows(rows)
    return response
