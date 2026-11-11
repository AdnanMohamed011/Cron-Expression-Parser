def parse_field(field_str, min_val, max_val):

    if "/" in field_str:
        sliced_str = field_str.split("/")
        if len(sliced_str) != 2:
            raise ValueError("Invalid value!")

        if sliced_str[0] == "" or sliced_str[1] == "":
            raise ValueError("Both start and step value are required!")

        try:
            if sliced_str[0] != "*":
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
    
            



# cron_fields = [("60", 0, 59),       # Above maximum
#     ("-1", 0, 59),       # Negative number
#     ("abc", 0, 59),      # Invalid characters
#     ("1.5", 0, 59),      # Decimal number
#     ("5-", 0, 59),       # Missing range endpoint
#     ("10-5", 0, 59),     # Reversed range
#     ("*/0", 0, 59),      # Zero step
#     ("*/", 0, 59),       # Missing step value
#     ("1,,3", 0, 59),     # Empty list item
#     ("*/2/3", 0, 59)]     # Multiple slash operators


# for expression, min_val, max_val in cron_fields:
#     try:
#         result = parse_field(expression, min_val, max_val)
#         print(f"{expression}: UNEXPECTED RESULT: {result}")
#     except ValueError as e:
#         print(f"{expression}: Correctly rejected: {e}")