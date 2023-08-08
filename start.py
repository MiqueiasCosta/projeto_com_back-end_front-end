from funcoes import checking

parsing_json = checking()
if parsing_json == True or False:
    from lista import listing_
    listing_()
    from hora_data import change_window
    if change_window == True:
        from principal import loop
        loop()
elif parsing_json == '++':
    from principal import loop
    loop()

