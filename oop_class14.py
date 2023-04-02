class Country:
    def __init__(self, name: str, population: int, capital=None):
        self.name = name
        self.population = population

        # check if user passed capital arg and check if it is a string
        if capital is not None and not isinstance(capital, str):
            raise TypeError("Capital must be a string.")
        # adding third instance
        self.capital = capital

    # magic method
    def __str__(self):
        return f'Country: {self.name} with population {self.population}'

    def __eq__(self, args):  # comparing
        print(self.name, self.population)
        print(args.name, args.population)
        return self.population == args.population

    def increase_population(self, value):
        """Method take argument and increase population of the country
        on this number."""
        inc = self.population * value
        return inc

    def add(self, other_country):
        """Create another country object with the name
        of the two countries combined and population
        of the two countries added together."""
        combined_name = self.name + ' ' + other_country.name
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

    def __add__(self, other):
        """Implement previous method as a magic one."""
        if not isinstance(other, Country):
            raise TypeError("Can only combine Countries objects.")
        combined_name = self.name + ' ' + other.name
        combined_population = self.population + other.population
        capital = self.capital or other.capital
        return Country(combined_name, combined_population, capital)


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

combined_country = bosnia.add(herzegovina)
print(combined_country)

england = Country('England', 55_000_000, 'London')
ireland = Country('Ireland', 5_000_000, 'Dublin')
scotland = Country('Scotland', 5_400_000, 'Edinburg')

combined_country2 = england + ireland + scotland
print(combined_country2)
