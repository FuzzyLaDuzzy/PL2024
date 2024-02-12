import sys

# Lê linhas da entrada padrão
lines = sys.stdin.readlines()
data = [line.strip().split(',') for line in lines]


#Lista ordenada alfabeticamente pela modalidade
header = data[0]
modalidade_index = header.index('modalidade')
sorted_data = sorted(data[1:], key=lambda x: x[modalidade_index])
for row in [header] + sorted_data:
    print(row)

print("\n")

#Percentagem de Atletas Aptos e Inaptos
header2 = data[0]
federado_index = header2.index('federado')

fit_count = sum(1 for row in data[1:] if row[federado_index] == 'true')
unfit_count = sum(1 for row in data[1:] if row[federado_index] == 'false')

total_athletes = len(data) - 1
fit_percentage = (fit_count / total_athletes) * 100
unfit_percentage = (unfit_count / total_athletes) * 100
print(f"Número de Atletas: {total_athletes}")
print(f"Atletas Aptos: {fit_count} ({fit_percentage:.2f}%)")
print(f"Atletas Inaptos: {unfit_count} ({unfit_percentage:.2f}%)\n")


#Distribuição de Atletas por Escalão (Intervalos de 5 anos)
header3 = data[0]
idade_index = header.index('idade')

age_groups = {
    '20-24': 0,
    '25-29': 0,
    '30-34': 0,
    '35-39': 0,
}

for row in data[1:]:
    age = int(row[idade_index])
    for group in age_groups:
        lower, upper = map(int, group.split('-'))
        if lower <= age <= upper:
            age_groups[group] += 1
            break

print("Distribuição de atletas por Escalão:")
for group, count in age_groups.items():
    print(f"{group}: {count}")

print("\n")
