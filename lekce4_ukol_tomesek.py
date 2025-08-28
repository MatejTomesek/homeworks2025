# Vytvořte tři proměnné: věk kupujícího, jeho aktuální zůstatek peněz a cenu piva. Napište podmínku, která rozhodne, zda si uživatel může koupit pivo. Hodnoty všech proměnných můžete zadat v programu staticky, nebo je dynamicky přijmout z uživatelského vstupu. Pokud si uživatel může pivo koupit, vypiš jeho zůstatek peněz po nákupu.
#
# Pokud si pivo může koupit, vypište například:
# "Můžeš si koupit pivo! Zůstatek peněz na účtu: 320Kč"
# Pokud si ho koupit nemůže, vypište odpovídající zprávu, například:
# "Nemůžeš si koupit pivo: nesplňuješ podmínky."

customer_age = int(input("Enter your age: "))
current_budget = int(input("Enter your current budget: "))
beer_price = int(input("Enter beer price: "))
remaining_budget = current_budget - beer_price20

if customer_age >= 18:
    if beer_price <= current_budget:
        print("You can buy beer! Remaining budget: ", remaining_budget)
    else:
        print("Sorry, you don't have enough money!")
else:
    print("Sorry, you can not buy beer!")
