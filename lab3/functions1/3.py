def how_many(heads,legs):
    heads=int(heads)
    legs=int(legs)
    rabbits=(legs-heads*2)/2
    chickens=heads-rabbits
    return rabbits,chickens
heads=input()
legs=input()
chickens,rabbits=how_many(heads,legs)
print(f"{rabbits} rabbits and {chickens} chickens")