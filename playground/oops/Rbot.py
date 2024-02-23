#!/usr/bin/python3
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    #def __getattr__(self, name):
       # return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        if name == 'name':
            if value in ['Henry', 'Oscar']:
                raise ValueError('Not a decent Robot name')
            elif name == 'build_year':
                if int(value) < 2020:
                    raise ValueError('Build Year has to be after 2019')
            self.__dict__[f"__{name}"] = value


robot = Robot("MArvin", 2020, "techcity")
rot = Robot("MAtt", "1902", "waxoon")
bot = Robot("Hen", "2020", "techcity")

print(robot.name)
print(robot.build_year)
print(robot.city)

print(rot.name)
print(rot.build_year)
print(rot.city)

print(bot.name)
print(bot.build_year)
print(bot.city)
