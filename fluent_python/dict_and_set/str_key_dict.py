

class StrKeyDict(dict):
    
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

if __name__ == "__main__":
    # d = StrKeyDict([("2", "two"), ("3", "three")])
    d  = StrKeyDict({"2": "two", "3": "three"})
    print(d)
    print(d["2"])
    print(d[3])
    print(d.get("2"))
    print(d.get(3))
    print(2 in d)
    print(4 in d)
