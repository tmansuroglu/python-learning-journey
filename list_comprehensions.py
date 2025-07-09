print(
    [
        x**3
        for x in [
            1,
            2,
            3,
        ]
    ]
)

print(list(map(lambda x: x**2, range(10))))

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])  # a nested loop

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
