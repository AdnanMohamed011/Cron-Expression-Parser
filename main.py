import argparse

def parse_field(field_str, min_val, max_val):

    if "/" in field_str:
        sliced_str = field_str.split("/")
        if len(sliced_str) != 2:
            raise ValueError("Invalid value!")

        if sliced_str[0] == "" or sliced_str[1] == "":
            raise ValueError("Both start and step value are required!")

        try:
            if sliced_str[0] == "*" or "-" in sliced_str[0]:
                pass
            else:
                int(sliced_str[0])
                int(sliced_str[1])
        except ValueError:
            raise ValueError("Value cannot be converted to an integer!")
        
        if int(sliced_str[1]) <= 0:
            raise ValueError("Step salue cannot be lesser or equal to 0 !")

        if sliced_str[0] == "" or sliced_str[1] == "":
            raise ValueError("Invalid value!")
        if "-" in sliced_str[0]:
            range_num = sliced_str[0].split("-")
            if len(range_num) != 2:
                raise ValueError("Invalid value!")
            try:
                int(range_num[0])
                int(range_num[1])
            except ValueError:
                raise ValueError("Value cannot be converted to an integer!")
            
            num1 = int(range_num[0])
            num2 = int(range_num[1])
            return list(range(num1, num2+1, int(sliced_str[1])))

        elif "*" == sliced_str[0]:
            return list(range(min_val, max_val+1, int(sliced_str[1])))
        
        num = int(sliced_str[0])
        step = int(sliced_str[1])
        return list(range(num, max_val+1, step))

    elif "-" in field_str:
        if "-" == field_str[0]:
            raise ValueError("Value cannot be negative!")
        
        range_num = field_str.split("-")
        if len(range_num) != 2:
            raise ValueError("Invalid value! 4")

        if range_num[0] == "" or range_num[1] == "":
            raise ValueError("Both start and end range value are required!")

        try:
            int(range_num[0])
            int(range_num[1])
        except ValueError:
            raise ValueError("Value cannot be converted to an integer!")
        
        num1 = int(range_num[0])
        num2 = int(range_num[1])
        if num1 > num2:
            raise ValueError("Start range value cannot be greater that end range value!")
        if num1 < min_val or num2 > max_val:
            raise ValueError("Value not in range!")
        return list(range(num1, num2+1))

    elif "," in field_str:
        nums = field_str.split(",")
        if len(nums) < 1:
            raise ValueError("Invalid value!")
        
        list_num = []
        for num in nums:
            if num == "":
                raise ValueError("Invalid value!")
            
            try:
                int(num)
            except ValueError:
                raise ValueError("Value cannot be converted to an integer!")

            if int(num) < min_val or int(num) > max_val:
                raise ValueError("Value not in range!")
            
            list_num.append(int(num))
        return sorted(list_num)

    elif "*" == field_str:
        return list(range(min_val, max_val+1))

    else:
        try:
            int(field_str)
        except ValueError:
            raise ValueError("Value cannot be converted to an integer!")
        
        if int(field_str) < min_val or int(field_str) > max_val:
            raise ValueError("Value is out of range!")
        
        return [int(field_str)]
    
            
def expand_cron(cron_string):
    if not isinstance(cron_string, str):
        raise ValueError("Cron expression must be a string")
    
    cron = cron_string.split()
    if len(cron) != 5:
        raise ValueError("Invalid cron expression!")

    cron_dict = {
        "minute": parse_field(cron[0], 0, 59),
        "hour": parse_field(cron[1], 0, 23),
        "day_of_month": parse_field(cron[2], 1, 31),
        "month": parse_field(cron[3], 1, 12),
        "day_of_week": parse_field(cron[4], 0, 6)
    }
    return cron_dict


def format_output(expanded):
    for cron, parse in expanded.items():
        print(f"{cron:<14}| {parse}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("cron")

    args = parser.parse_args()

    cron_expression = expand_cron(args.cron)
    format_output(cron_expression)