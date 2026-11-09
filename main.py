def parse_field(field_str, min_val, max_val):
    if "/" in field_str:
        sliced_str = field_str.split("/")
        if len(sliced_str) != 2:
            raise ValueError("Invalid value!")
        try:
            int(sliced_str[0])
            int(sliced_str[1])
        except ValueError:
            raise ValueError("Invalid value!")
        
        if "-" in sliced_str[0]:
            range_num = sliced_str[0].split("-")
            try:
                int(range_num[0])
                int(range_num[1])
            except ValueError:
                raise ValueError("Invalid value!")
            num1 = int(range_num[0])
            num2 = int(range_num[1])
            return list(range(num1, num2+1, int(sliced_str[1])))

        elif "*" == sliced_str[0]:
            return list(range(min_val, max_val+1, int(sliced_str[1])))
        
        num = int(sliced_str[0])
        step = int(sliced_str[1])
        return list(range(num, max_val+1, step))

print(parse_field("q/5", 1, 31))
print(parse_field("5-45/10", 0, 59))
print(parse_field("*/2", 1, 12))
