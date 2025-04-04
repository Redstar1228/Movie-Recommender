# Movie-Recommender
from random import choice

try:
    films = {
        "gravity_falls": {
            "author": "disney",
            "action": False,
            "adventure": True,
            "comedy": True,
            "drama": False,
            "fantasy": True,
            "horror": False
        },
        "spongebob": {
            "author": "nickelodeon",
            "action": False,
            "adventure": True,
            "comedy": True,
            "drama": False,
            "fantasy": False,
            "horror": False
        },
        "titans": {
            "author": "warner",
            "action": True,
            "adventure": False,
            "comedy": True,
            "drama": False,
            "fantasy": True,
            "horror": False
        },
        "scooby_doo": {
            "author": "warner",
            "action": True,
            "adventure": True,
            "comedy": True,
            "drama": False,
            "fantasy": False,
            "horror": False
        },
        "boss_baby": {
            "author": "dreamworks",
            "action": False,
            "adventure": True,
            "comedy": True,
            "drama": False,
            "fantasy": True,
            "horror": False
        },
        "simpsons": {
            "author": "fox",
            "action": False,
            "adventure": False,
            "comedy": True,
            "drama": True,
            "fantasy": False,
            "horror": False
        },
        "patmat": {
            "author": "kratky",
            "action": False,
            "adventure": False,
            "comedy": True,
            "drama": False,
            "fantasy": False,
            "horror": False
        },
        "dragon": {
           "author": "dreamworks",
           "action": True,
            "adventure": True,
            "comedy": False,
            "drama": False,
            "fantasy": True,
            "horror": False
        }
    }
    nums = []
    def solve(x):
        y = ""
        oth = ""
        for k, v in films.items():
            exec(f"{k} = []")
            for i, ii in v.items():
                exec(f"{k}.append(ii)")
        for genre, v in films[x].items():
            exec(f"{genre} = []")
        for i, ii in films.items():
            for iii, iv in ii.items():
                if iv:
                    eval(f"{iii}.append(i)")
        for genre, v in films[x].items():
            if x in eval(genre):
                eval(f"{genre}.remove(x)")
                y += str(eval(genre))
        for i, ii in enumerate(films):
            if ii in y:
                nums.append(ii)
        for k in films:
            if films[k]["author"] == films[x]["author"] and k != x:
                z = k
                break
            else:
                z = nums[len(nums) - 2]
        res = f"{z} and {nums[len(nums) - choice([1, 3])]}"
        result = f"\ntry {res}!"
        print(result)
    print("do you like which one?")
    for i in films:
        print(i)
    x = input("──────────────────\n")
    if x in films:
        solve(x)
    else:
        print("Invalid film")
except Exception as err:
    print(err)
