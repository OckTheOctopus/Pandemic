# Name doesn't need much explaination
def run_pandemic(vaccine_rollout_wave):
    # Needed variables
    population = 1000000
    spreaders = 0
    superspreaders = 0
    total_dead = 0
    total_infected = superspreaders + spreaders

    in_lockdown = False
    vaccine_being_rolled_out = False
    vaccinated = 0
    vaccine_ratio = 0 # The 2.5% of people every wave to be vaccinated

    infectable = population - total_infected - vaccinated

    for wave in range(1, 101):
        if wave == vaccine_rollout_wave:
            vaccine_ratio = round(population * 0.025)
        dead_this_wave = 0
        asymptomatic = 0

        if wave >= 1 and wave < 4:
            in_lockdown = True
        else:
            in_lockdown = False

        if wave >= vaccine_rollout_wave:
            vaccine_being_rolled_out = True


        if wave == 1:
            spreaders = 12
            superspreaders = 5

            asymptomatic = round(spreaders * 0.5)
            isolated = round(spreaders * 0.35)
            dead_this_wave = round(spreaders * 0.075)

            population -= dead_this_wave
            total_dead += dead_this_wave
            total_infected = superspreaders + spreaders
            infectable = population - total_infected - vaccinated
        else:
            if in_lockdown:
                prevSpreaders = spreaders

                if prevSpreaders <= 0:
                    spreaders = 0
                else:
                    spreaders = round((asymptomatic + (infectable * 0)) - prevSpreaders)
                    if spreaders < 0:
                        spreaders = 0
                    dead_this_wave = round(prevSpreaders * 0.0375)
                    population -= dead_this_wave
                    total_dead += dead_this_wave
                    total_infected = superspreaders + spreaders
                    infectable = population - total_infected - vaccinated

                superspreaders = round(superspreaders + (infectable * 0.00001))
                total_infected = superspreaders + spreaders
                infectable = population - total_infected - vaccinated
            else:
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
                    infectable = population - total_infected - vaccinated

                if vaccine_being_rolled_out:
                    vaccinated += vaccine_ratio

                    if vaccinated > population:
                        vaccinated = population
                        vaccine_ratio = 0

    results = {
        'superspreaders': superspreaders,
        'dead': total_dead,
        'vaccinated': vaccinated
    }

    return results

for i in range(20, 101):
    data = run_pandemic(i)
    print('-' * 10)
    print(f"""Wave vaccine rolled out: {i}
Superspreaders: {data['superspreaders']}
Dead: {data['dead']}
Vaccinated: {data['vaccinated']}""")
