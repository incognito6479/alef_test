from urllib.request import urlopen
import re
from mainapp.models import CityInfo


def test():
    CityInfo.objects.all().delete()
    url = "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    tbody = re.findall(r"<tbody>(.*?)</tbody>", html)[0]
    tr = re.findall(r"<tr(.*?)>(.*?)</tr>", tbody)
    td = []
    for i in tr:
        td.append(re.findall(r"<td(.*?)>(.*?)</td>", i[1]))
    for row in td:
        for index in range(0, len(row)):
            row[index] = row[index][1]
            if index == 1:
                row[index] = re.findall(r'"(.*?)"', row[index])
    bulk_creator = []
    del td[0]
    for row in td:
        row.insert(5, re.sub(r"<.*?>", " ", row[4]).split(" ")[4])
        row[5] = re.sub(r"&.*?;", "", row[5])
        row[4] = re.sub(r"<.*?>", " ", row[4]).split(" ")[2]
        row[4] = re.sub(r"&.*;", "", row[4])
        if "-" in row[6]:
            row[6] = row[6].split("-")[0]
        bulk_creator.append(
            CityInfo(
                id_from_page=row[0],
                url=f"https://ru.wikipedia.org/{row[1][0]}",
                city_name=row[1][1],
                okato=row[3].replace(" ", ""),
                population=int(row[4]) * pow(10, int(row[5])),
                founded_in=row[6],
                status_of_city=row[7]
            )
        )
    CityInfo.objects.bulk_create(bulk_creator)
    return

