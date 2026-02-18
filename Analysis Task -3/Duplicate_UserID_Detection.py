user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]
id_count = {}
for user in user_ids:
    if user in id_count:
        id_count[user] += 1
    else:
        id_count[user] = 1

for user, count in id_count.items():
    if count > 1:
        print(f"{user} → {count} times")
