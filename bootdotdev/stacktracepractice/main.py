def create_stats_message(strength, wisdom, dexterity):  #stack trace aka traceback error
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
