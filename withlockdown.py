# Function is based of normalconditions.py and code is edited to implement the lockdown feature
def implement_lockdown(lockdown_wave, lockdown_lifted_wave):
    # Variables that are needed
    in_lockdown = False
    population = 1000000
    spreaders = 0
    superspreaders = 0
    total_dead = 0
    total_infected = superspreaders + spreaders
    infectable = population - total_infected

    for wave in range(1, 101):
        # Checks if in lockdown
        if wave >= lockdown_wave and wave < lockdown_lifted_wave:
            in_lockdown = True
        else:
            in_lockdown = False

        # The real magic happens here
        dead_this_wave = 0
        asymptomatic = 0

        if wave == 1:
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
            if in_lockdown:
                prevSpreaders = spreaders

                if prevSpreaders <= 0:
                    spreaders = 0
                else:
                    spreaders = round((asymptomatic + (infectable * 0)) - prevSpreaders)
                    #print(spreaders)
                    if spreaders < 0:
                        spreaders = 0
                    dead_this_wave = round(prevSpreaders * 0.0375)
                    population -= dead_this_wave
                    total_dead += dead_this_wave
                    total_infected = superspreaders + spreaders
                    infectable = population - total_infected
                
                superspreaders = round(superspreaders + (infectable * 0.00001))
                total_infected = superspreaders + spreaders
                infectable = population - total_infected

            else:
                # Shamelessly copy-pasted from normalconditions.py
                prevSpreaders = spreaders

                if prevSpreaders <= 0:
                    spreaders = 0
                else:
                    spreaders = round((asymptomatic + (infectable * 0.0001)) - prevSpreaders)
                    # Just in case we get negative spreaders
                    #print(spreaders)
                    if spreaders < 0:
                        spreaders = 0
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
        
    results = {
        'spreaders': spreaders,
        'superspreaders': superspreaders,
        'dead': total_dead
    }

    return results

for i in range(1, 101):
    data = implement_lockdown(i, i+3)
    print('-' * 10)
    print(f"""Lockdown implemented: {i}
Spreaders: {data['spreaders']}
Superspreaders: {data['superspreaders']}
Total dead: {data['dead']}""")
    print('-' * 10)