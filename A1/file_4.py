import redis

r = redis.Redis()

# ------------------------------
# Just Key/Value
print("--- Key/Value ---")
the_key = "user:1000"

## Create
r.set(the_key, "password")

## Read
print(r.get(the_key))

## Update
r.set(the_key, "nopassword")
print(r.get(the_key))

## Delete
r.delete(the_key)
print(r.get(the_key))

print("--- Key/Value ---")

# ------------------------------
# Just List
print("--- List ---")
the_list = "todolist"
## Create
r.rpush(the_list, "make acquaintance with Redis")

## Read
print(r.lrange(the_list, 0, -1))

## Update
r.rpush(the_list, "make acquaintance with MongoDB")
r.rpush(the_list, "find out how to work with Redis via Python")
print(r.lrange(the_list, 0, -1))

## Delete
r.lpop(the_list)
print(r.lrange(the_list, 0, -1))

print("--- List ---")
# ------------------------------
# Just Set
print("--- Set ---")
the_set = "math functions"

## Creating and Reading
r.sadd(the_set, "sin", "cos", "tan", "ctg")
print(r.smembers(the_set))

## Updating
r.sadd(the_set, "sec", "cosec", "cat")
print(r.smembers(the_set))

## Deleting
r.srem(the_set, "cat")
print(r.smembers(the_set))
print("--- Set ---")
