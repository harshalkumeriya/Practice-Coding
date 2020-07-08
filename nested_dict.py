input_dict = {'Fruit':1,'Vegetable':{'cauliflower':2,'cabbage':3},'Spices':4}
def flatten_dict(d):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + '_' + k, v) for k, v in flatten_dict(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)

out1=list(flatten_dict(input_dict).keys())
out2=list(flatten_dict(input_dict).values())
out1.sort()
out2.sort()
print(out1)
print(out2)


