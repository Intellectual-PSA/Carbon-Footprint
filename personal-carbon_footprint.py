import pandas as pd

class CarbonTracker:
    def __init__(self, name):
        self.name = name
        self.activities = pd.DataFrame(columns=['activity', 'quantity', 'carbon'])

    # Assuming we have a database or API from where we can fetch carbon emission data
    carbon_emission_factors = {
        'driving': 2.4,  # kg of CO2 per mile
        'flight': 0.18,  # kg of CO2 per km
        'meat_diet': 2.5,  # kg of CO2 per day
        'vegan_diet': 1.5,  # kg of CO2 per day
        # Add as many activities/items as available
    }

    def add_activity(self, activity, quantity):
        if activity in self.carbon_emission_factors:
            carbon_emission = self.carbon_emission_factors[activity] * quantity
            self.activities = self.activities.append({
                'activity': activity,
                'quantity': quantity,
                'carbon': carbon_emission}, 
                ignore_index=True)
        else:
            print("Sorry, we don't have data for that activity.")
    
    def get_total_footprint(self):
        return self.activities['carbon'].sum()

# Usage
person = CarbonTracker('John')
person.add_activity('driving', 10)  # John drove 10 miles
person.add_activity('flight', 300)  # John took a flight of 300 km
person.add_activity('meat_diet', 7)  # John followed a meat diet for a week
print(person.get_total_footprint())  # This will print John's total carbon footprint
