def flatten_helper(d, flat_dict, path):
    if not isinstance(d, dict):
        flat_dict[path] = d
        return 

    for key, val in d.items():
        new_key = f"{path}.{key}" if path else key
        flatten_helper(val, flat_dict, new_key)


def flatten(d):
    flat_dict = {}
    flatten_helper(d, flat_dict, '')

    return flat_dict

if __name__ == '__main__':
    d = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    new_dict = flatten(d)
    print(new_dict)
