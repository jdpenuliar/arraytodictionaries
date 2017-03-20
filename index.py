movies = [[1,"A"],  [2,"A"], [2,"B"], [3,"C"]]
users = [[1,2],  [1,3], [2,1]]



context = {
        }
for x in range (0,len(users)):
    if not context.get(users[x][0]):
        context[users[x][0]] = []

    for y in range (0,len(movies)):
        if users[x][1] == movies[y][0]:
            context[users[x][0]].append(movies[y][1])

print ("lol---\n", context)
