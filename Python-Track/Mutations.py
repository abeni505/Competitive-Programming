def mutate_string(string, position, character):
    str_list=list(string)
    str_list[position] = character
    new_str="" .join(str_list)
    return new_str
