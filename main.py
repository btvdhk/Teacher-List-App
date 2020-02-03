print("Welcome to the favourite Teachers App")
favteacher = []

favteacher.append(input("Who is your first favourite teacher: ").title())
favteacher.append(input("Who is your second favourite teacher: ").title())
favteacher.append(input("Who is your third favourite teacher: ").title())
favteacher.append(input("Who is your fourth  favourite teacher: ").title())

print(f"\nYour favourite teachers ranked are: {favteacher} ")
print(f"Your favourite teachers alphabetically are: {sorted(favteacher)} ")
print(f"Your favourute teachers reverse are: {sorted(favteacher, reverse=True)}")
print(f"\nYour top two teachers are: {favteacher[0]} and {favteacher[1]}")
print(f"\nYour next two teachers are: {favteacher[2]} and {favteacher[3]}")
print(f"\nYour last teacher are: {favteacher[-1]}")
print(f"\nYour have total {len(favteacher)} teachers")

favteacher.insert(0, input(f"\nOpps, {favteacher[0]} is no longer, Who is new? "))

print(f"\nYour favourite teachers ranked are: {favteacher} ")
print(f"Your favourite teachers alphabetically are: {sorted(favteacher)} ")
print(f"Your favourute teachers reverse are: {sorted(favteacher, reverse=True)}")
print(f"\nYour top two teachers are: {favteacher[0]} and {favteacher[1]}")
print(f"\nYour next two teachers are: {favteacher[2]} and {favteacher[3]}")
print(f"\nYour last teacher are: {favteacher[-1]}")
print(f"\nYour have total {len(favteacher)} teachers")

favteacher.remove(input("\nWhich teacher would you like to remove from your list: ").title())

print(f"\nYour favourite teachers ranked are: {favteacher} ")
print(f"Your favourite teachers alphabetically are: {sorted(favteacher)} ")
print(f"Your favourute teachers reverse are: {sorted(favteacher, reverse=True)}")
print(f"\nYour top two teachers are: {favteacher[0]} and {favteacher[1]}")
print(f"\nYour next two teachers are: {favteacher[2]} and {favteacher[3]}")
print(f"\nYour last teacher are: {favteacher[-1]}")
print(f"\nYour have total {len(favteacher)} teachers")
