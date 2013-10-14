
from urllib.request import urlopen
import re

REGEX_NUMBER = "<td class=\"resRoute\">\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t([0-9]+)"
REGEX_DEST = "<td class=\"resDir\" style=\"width:50%;\">(.+)&"
REGEX_DUE = "<td class=\"resDue\">([0-9]+) min<\/td>"

URL_STMARY = "http://m.countdown.tfl.gov.uk/arrivals/71024"
URL_ESSEX = "http://m.countdown.tfl.gov.uk/arrivals/75045"

class BusDataReader(object):

    def __init__(self):
        self.regex_number = REGEX_NUMBER
        self.regex_dest = REGEX_DEST
        self.regex_due = REGEX_DUE
        self.urls = [URL_ESSEX,URL_STMARY]
        self.valid_routes = ['4','56']
        self.valid_dest = ['Waterloo', 'St Bartholomews']

    def read_data(self):
        result = []
        for url in self.urls:
            # read data in until we get some data back
            # protect against empty/miss reads
            while True:
                # read data
                html = urlopen(url).read().decode('utf8')

                # extract data
                bus_number = re.findall(self.regex_number,html)
                bus_dest = re.findall(self.regex_dest,html)
                bus_due = re.findall(self.regex_due,html)

                if bus_number:
                 result.extend(zip(bus_number,
                                   bus_dest,
                                   [int(i) for i in bus_due]))
                 break
        return result

    def filterroutes(self,r):
        num, dest, due = r
        return (num in self.valid_routes) and (dest in self.valid_dest)

    def get_data(self):
        filtered_results = [t for t in self.read_data()
                            if self.filterroutes(t)]
        return sorted(filtered_results,key=lambda x: x[2])

def test():
    dbo = busdatareader()
    print (dbo.get_data())

if __name__ == '__main__':
    test()

