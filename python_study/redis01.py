import redis


def main():
    client = redis.Redis(host="", port=6379, password="")
    client.set("username", "hellokitty", ex=300)
    print(client.ttl("username"))
    print(client.get("username").decode())
    client.set("nickname", "罗永浩")
    print(client.get("nickname").decode())
    client.hset("stu1", "id", "1001")
    client.hset("stu1", "name", "罗永浩")


if __name__ == '__main__':
    main()