def resource_monitor(resources):
    overused = []

    for resource, hours in resources.items():
        if hours > 8:
            overused.append(resource)

    if overused:
        print("Overused Resources:", ", ".join(overused))
        print("Energy Alert: Yes")
    else:
        print("Overused Resources: None")
        print("Energy Alert: No")


usage = {
    "Projector": 6,
    "AC": 9,
    "Lights": 4
}

resource_monitor(usage)