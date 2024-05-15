
def how_many_panels_in_rectangle(a, b, x, y):
    # Placing panels oriented as a x b
    fit_x_ab = x // a
    fit_y_ab = y // b
    panels_installed_ab = fit_x_ab * fit_y_ab
    remaining_x_ab = x % a
    remaining_y_ab = y % b
    
    if remaining_x_ab == 0 and remaining_y_ab == 0:
        return panels_installed_ab
    
    area_left_1_ab = (remaining_x_ab, y)
    area_left_2_ab = (x, remaining_y_ab)
    
    # Calculating extra panels when rotated. Extra panels are not added directly
    # because the areas left intersect, and the maximum is taken instead.
    extra_panels_1_ab = (area_left_1_ab[0] // b) * (area_left_1_ab[1] // a)
    extra_panels_2_ab = (area_left_2_ab[0] // b) * (area_left_2_ab[1] // a)
    panels_installed_ab += max(extra_panels_1_ab, extra_panels_2_ab)
    
    # Placing panels oriented as b x a
    fit_x_ba = x // b
    fit_y_ba = y // a
    panels_installed_ba = fit_x_ba * fit_y_ba
    remaining_x_ba = x % b
    remaining_y_ba = y % a

    if remaining_x_ba == 0 and remaining_y_ba == 0:
        return panels_installed_ba
    
    area_left_1_ba = (remaining_x_ba, y)
    area_left_2_ba = (x, remaining_y_ba)
    
    # Calculating extra panels when rotated. Extra panels are not added directly
    # because the areas left intersect, and the maximum is taken instead.
    extra_panels_1_ba = (area_left_1_ba[0] // a) * (area_left_1_ba[1] // b)
    extra_panels_2_ba = (area_left_2_ba[0] // a) * (area_left_2_ba[1] // b)
    panels_installed_ba += max(extra_panels_1_ba, extra_panels_2_ba)
    
    return max(panels_installed_ab, panels_installed_ba)


print(how_many_panels_in_rectangle(1,2,3,5))
print(how_many_panels_in_rectangle(2,2,3,5))
print(how_many_panels_in_rectangle(1,2,2,4))
print(how_many_panels_in_rectangle(2,2,1,10))


# Cosas que se podrían mejorar:
# En lugar de dividir el triangulo en tiras de largo a o dividirlo en tiras de largo b
# Se podría dividir en distintas combinaciones de largo a y b ya sí explorar más escenarios posibles
def how_many_panels_in_isc_triangle(a, b, base, height):
    # Placing panels oriented as a x b
    # We will divide the triangle into horizontal strips of height b
    # untill the width is lower than 'a'

    def strip_width(i, strip_height):
        strip_width = base * (1 - (strip_height * i / height))
        return strip_width
    
    # starting with i = 1, first strip from the base
    i = 1
    strip_w = strip_width(i, b)
    if strip_w < a:
        return 0
    rectangular_strips = []
    max_possible_strips = height // b
    while strip_w > a and len(rectangular_strips) < max_possible_strips:
        strip = (strip_w, b)
        rectangular_strips.append(strip)
        i += 1
        strip_w = strip_width(i, b)

    # We use our previous function to calculate amount of panels for each strip
    panels_installed_ab = 0
    for strip in rectangular_strips:
        panels_to_install = how_many_panels_in_rectangle(a, b, strip[0], strip[1])
        panels_installed_ab += panels_to_install
    
    # Placing panels oriented as b x a
    # starting with i = 1, first strip from the base
    i = 1
    strip_w = strip_width(i, a)
    if strip_w < b:
        return 0
    rectangular_strips = []
    max_possible_strips = height // a
    while strip_w > b and len(rectangular_strips) < max_possible_strips:
        strip = (strip_w, a)
        rectangular_strips.append(strip)
        i += 1
        strip_w = strip_width(i, a)

    # We use our previous function to calculate amount of panels for each strip
    panels_installed_ba = 0
    for strip in rectangular_strips:
        panels_to_install = how_many_panels_in_rectangle(b, a, strip[0], strip[1])
        panels_installed_ba += panels_to_install

    return max(panels_installed_ab, panels_installed_ba)


print(how_many_panels_in_isc_triangle(2, 3, 10, 17))





    


    

    
    

    