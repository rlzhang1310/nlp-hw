import time

from guesser import Guesser
from collections import defaultdict
from datetime import datetime

kPRESIDENT_DATA = {"train": [
  {"start": 1789, "stop": 1797, "name": "George Washington"},
  {"start": 1797, "stop": 1801, "name": "John Adams"},
  {"start": 1801, "stop": 1809, "name": "Thomas Jefferson"},
  {"start": 1809, "stop": 1817, "name": "James Madison"},
  {"start": 1817, "stop": 1825, "name": "James Monroe"},
  {"start": 1825, "stop": 1829, "name": "John Quincy Adams"},
  {"start": 1829, "stop": 1837, "name": "Andrew Jackson"},
  {"start": 1837, "stop": 1841, "name": "Martin Van Buren"},
  {"start": 1841, "stop": 1841, "name": "William Henry Harrison"},
  {"start": 1841, "stop": 1845, "name": "John Tyler"},
  {"start": 1845, "stop": 1849, "name": "James K. Polk"},
  {"start": 1849, "stop": 1850, "name": "Zachary Taylor"},
  {"start": 1850, "stop": 1853, "name": "Millard Fillmore"},
  {"start": 1853, "stop": 1857, "name": "Franklin Pierce"},
  {"start": 1857, "stop": 1861, "name": "James Buchanan"},
  {"start": 1861, "stop": 1865, "name": "Abraham Lincoln"},
  {"start": 1865, "stop": 1869, "name": "Andrew Johnson"},
  {"start": 1869, "stop": 1877, "name": "Ulysses S. Grant"},
  {"start": 1877, "stop": 1881, "name": "Rutherford Birchard Hayes"},
  {"start": 1881, "stop": 1881, "name": "James A. Garfield"},
  {"start": 1881, "stop": 1885, "name": "Chester A. Arthur"},
  {"start": 1885, "stop": 1889, "name": "Grover Cleveland"},
  {"start": 1889, "stop": 1893, "name": "Benjamin Harrison"},
  {"start": 1893, "stop": 1897, "name": "Grover Cleveland"},
  {"start": 1897, "stop": 1901, "name": "William McKinley"},
  {"start": 1901, "stop": 1905, "name": "Theodore Roosevelt"},
  {"start": 1905, "stop": 1909, "name": "Theodore Roosevelt"},
  {"start": 1909, "stop": 1913, "name": "William H. Taft"},
  {"start": 1913, "stop": 1921, "name": "Woodrow Wilson"},
  {"start": 1921, "stop": 1923, "name": "Warren G. Harding"},
  {"start": 1923, "stop": 1929, "name": "Calvin Coolidge"},
  {"start": 1929, "stop": 1933, "name": "Herbert Hoover"},
  {"start": 1933, "stop": 1945, "name": "Franklin D. Roosevelt"},
  {"start": 1945, "stop": 1953, "name": "Harry S. Truman"},
  {"start": 1953, "stop": 1961, "name": "Dwight D. Eisenhower"},
  {"start": 1961, "stop": 1963, "name": "John F. Kennedy"},
  {"start": 1963, "stop": 1969, "name": "Lyndon B. Johnson"},
  {"start": 1969, "stop": 1974, "name": "Richard M. Nixon"},
  {"start": 1974, "stop": 1977, "name": "Gerald R. Ford"},
  {"start": 1977, "stop": 1981, "name": "Jimmy Carter"},
  {"start": 1981, "stop": 1989, "name": "Ronald Reagan"},
  {"start": 1989, "stop": 1993, "name": "George Bush"},
  {"start": 1993, "stop": 2001, "name": "Bill Clinton"},
  {"start": 2001, "stop": 2009, "name": "George W. Bush"},
  {"start": 2009, "stop": 2017, "name": "Barack Obama"},
  {"start": 2017, "stop": 2021, "name": "Donald J. Trump"},
  {"start": 2021, "stop": 2025, "name": "Joseph R. Biden"}],
  "dev": [{"text": "Who was president on Wed Jan 25 06:20:00 2023?", "page": "Joseph R. Biden", "qanta_id":201},
          {"text": "Who was president on Sat May 23 02:00:00 1982?", "page": "Ronald Reagan", "qanta_id":202},
          {"text": "Who was president on Wed Mar 01 04:23:40 2023?", "page": 'Joseph R. Biden', "qanta_id":203},
          {"text": "Who was president on Tue Jan 20 13:00:00 2009?", "page": 'Barack Obama', "qanta_id":204},
          {"text": "Who was president on Fri Nov 22 16:00:00 1963?", "page": 'Lyndon B. Johnson', "qanta_id":205},
          {"text": "Who was president on Tue Apr 12 20:00:00 1949?", "page": 'Harry S. Truman', "qanta_id":206},
          {"text": "Who was president on Sat Mar 04 21:00:00 1933?", "page": 'Franklin D. Roosevelt', "qanta_id":207},
          {"text": "Who was president on Sat Apr 15 15:00:00 1865?", "page": 'Andrew Johnson', "qanta_id":208},
          {"text": "Who was president on Thu Apr 30 17:00:00 1789?", "page": 'George Washington', "qanta_id":209}]
}

class PresidentGuesser(Guesser):
    def train(self, training_data):
        self._lookup = defaultdict(dict)
        for line in training_data:
            for i in range(line["start"], line["stop"]):
                self._lookup[str(i)] = line["name"]
        self._lookup["1788"] = 'George Washington'

    def __call__(self, question, n_guesses=1):
        # Update this code so that we can have a different president than Joe
        # Biden
        date_str = question[25:-1]
        date_format = "%b %d %H:%M:%S %Y"
        date = datetime.strptime(date_str, date_format)
        year = int(question[-5:-1])

        ## WILLIAM HENRY 3/4-4/4 1841
        ## JAMES GARFIELD 3/4-9/19 1881
        jan_twenty = datetime(year, 1, 20, 12, 0, 0)
        april_fifteen = datetime(year, 4, 15, 12, 0, 0)
        apr_twenty = datetime(year, 4, 20, 12, 0, 0)
        apr_twelth = datetime(year, 4, 12, 12, 0, 0)
        jul_ninth = datetime(year, 7, 9, 12, 0, 0)
        march_fourth = datetime(year, 3, 4, 12, 0, 0)
        april_fourth = datetime(year, 4, 4, 12, 0, 0)
        september_nineteen = datetime(year, 9, 19, 12, 0, 0)
        september_fourteen = datetime(year, 9, 14, 12, 0, 0)
        aug_second = datetime(year, 8, 2, 12, 0, 0)
        aug_ninth = datetime(year, 8, 9, 12, 0, 0)
        nov_twentytwo = datetime(year,11, 22, 12, 0, 0)
        if year == 1881 and date < september_nineteen and date > march_fourth:
            return [{"guess": "James A. Garfield"}]
        elif year == 1841 and date < april_fourth and date > march_fourth:
            return [{"guess": "William Henry Harrison"}]
        elif year == 1841 and date < apr_twenty:
            year -= 1
        elif year == 1850 and date < jul_ninth:
            year -= 1
        elif year == 1841 and date < april_fourth:
            year -= 1
        elif year == 1865 and date < april_fifteen:
            year -= 1
        elif year == 1881 and date < september_nineteen:
            year -= 1
        elif year == 1901 and date < september_fourteen:
            year -= 1
        elif year == 1923 and date < aug_second:
            year -= 1
        elif year == 1945 and date < apr_twelth:
            year -= 1
        elif year == 1963 and date < nov_twentytwo:
            year -= 1
        elif year == 1974 and date < aug_ninth:
            year -= 1
        elif year >= 1953 and date < jan_twenty:
            year -= 1
        elif year < 1953 and date < march_fourth:
            year -= 1

        candidates =  [self._lookup[str(year)]]
        if len(candidates) == 0:
            return [{"guess": ""}]
        else:
            return [{"guess": x} for x in candidates]

        
if __name__ == "__main__":
    pg = PresidentGuesser()

    pg.train(kPRESIDENT_DATA["train"])
    
    for date in kPRESIDENT_DATA["dev"]:
        print(date, pg(date)["guess"])
        
