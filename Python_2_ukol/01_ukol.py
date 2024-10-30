import csv
import json

dictionary=[]
input_tsv_file = './netflix_titles.tsv'
output_json_file = './hw02_output.json'

with open(input_tsv_file,'r', encoding='utf-8') as netflix_file:
    reader = csv.DictReader(netflix_file, delimiter='\t')

    for row in reader:

        title = row['PRIMARYTITLE']
        directors = row['DIRECTOR'].split(', ') if row['DIRECTOR'] else []
        cast = row['CAST'].split(', ') if row['CAST'] else []
        genres = row['GENRES'].split(',')
        start_year = int(row['STARTYEAR'])
        decade = (start_year // 10) * 10
        
        dictionary.append({
            "title": title,
            "directors": directors,
            "cast": cast,
            "genres": genres,
            "decade": decade
        })

with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(dictionary, json_file, indent=4, ensure_ascii=False)