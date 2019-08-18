import requests

# Wykonanie zapytania API i zachowanie otrzymanej odpowiedzi

url = 'https://api.github.com/search/repositories?q=/user:mskpm'

r = requests.get(url)
print('Kod stanu: ', r.status_code)



# Umieszczenie odpowiedzi API w zmiennej
response_dict = r.json()

print("Całkowita liczba repozytoriów:" , response_dict['total_count'])

# Przetwarzanie wyników
print(response_dict.keys())

# Przetwarzanie informacji o repozytoriach
repo_dicts = response_dict['items']
print("Liczba zwróconych repozytoriów: ", len(repo_dicts))

# Przeanalisowanie pierwszego repozytorium
repo_dict = repo_dicts[0]
print("\nKlucze: ", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)



