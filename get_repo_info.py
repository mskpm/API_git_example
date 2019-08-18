import datetime
import locale

class repo_info:
    """Przechowuje informacje o repozytorium"""
    def __init__(self, repo_dict):
        self.nazwa = repo_dict['name']
        self.wlasciciel = repo_dict['owner']['login']
        self.repozytorium = repo_dict['html_url']
        self.data_powstania = repo_dict['created_at']
        self.data_uakualizacji = repo_dict['updated_at']
        self.opis = repo_dict['description']

    def show(self):
        """Wyświetla opis repozytorium"""
        print('\nWybrane informacje o repozytorium: ' + self.nazwa)
        print('Właściciel: ' + self.wlasciciel)
        print('Rezpozytorium: ' + self.repozytorium)
        print('Utworzone: ', + self.data_powstania)
        print('Uakrualnione: ' + self.data_uakualizacji)
        print('Opis: ' + self.opis)

def repo_time(gtime):
    """Konwertuje format czasu z git"""
    time=datetime.datetime.strptime(gtime[0:9]+gtime[11:19], '%Y-%m-%d%H:%M:%S')
    return time

def show_info(repo_dict):
    """Wyświetla opis repozytorium"""
    print('\nWybrane informacje o repozytorium: ' + str(repo_dict['name']))
    print('Właściciel: ' + str(repo_dict['owner']['login']))
    print('Rezpozytorium: ' + str(repo_dict['html_url']))
    t=repo_time(repo_dict['created_at'])
    locale.setlocale(locale.LC_ALL, "pl_PL.utf8")
    print('Utworzone: ' + t.strftime('(%A) %d-%B-%Y %X').title())
    t=repo_time(repo_dict['updated_at'])
    print('Uaktualnione: ' + t.strftime('(%A) %d-%B-%Y %X').title())
    print('Opis: ' + str(repo_dict['description']))
