# Variables that we need. Names are pretty self explainatory
population = 1000000
spreaders = 0
superspreaders = 0
total_dead = 0
total_infected = superspreaders + spreaders
infectable = population - total_infected

# Waves 1-100
for i in range(1,101):
    # Will update when needed
    dead_this_wave = 0
    asymptomatic = 0

    if i == 1:
        spreaders = 12
        superspreaders = 5

        asymptomatic = round(spreaders * 0.5)
        isolated = round(spreaders * 0.35)
        dead_this_wave = round(spreaders * 0.075)

        population -= dead_this_wave
        total_dead += dead_this_wave
        total_infected = superspreaders + spreaders
        infectable = population - total_infected

    else:
        prevSpreaders = spreaders

        spreaders = round((asymptomatic + (infectable * 0.0001)) - prevSpreaders)
        asymptomatic = round(spreaders * 0.5)
        isolated = round(spreaders * 0.35)
        dead_this_wave = round(prevSpreaders * 0.075)

        population -= dead_this_wave
        total_dead += dead_this_wave
        total_infected = superspreaders + spreaders
        infectable = population - total_infected

        superspreaders = round(superspreaders + (infectable * 0.001))
        total_infected = superspreaders + spreaders
        infectable = population - spreaders - superspreaders

    print('-' * 10)
    print(f"""WAVE {i}: 
Spreaders: {spreaders}
Superspreaders: {superspreaders}
Dead this wave: {dead_this_wave}
Total dead: {total_dead}""")
    print('-' * 10)
