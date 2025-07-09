example = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key11": 11}
del example["key1"]
print(example)

print(list(example))  # returns the keys in insertion order
print(sorted(example))  # returns the keys in sorted way

example2 = dict([("key22", 22), ("key33", 33)])
print(example2)

print(
    {
        x: x**2
        for x in (
            2,
            3,
            4,
        )
    }
)
