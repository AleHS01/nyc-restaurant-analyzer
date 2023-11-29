import pandas as pd

class RestaurantData:
    def __init__(self, file_path):
        # Load data from the specified CSV file
        self.data_frame = pd.read_csv(file_path)

        # Process the DataFrame to get boroughs and their restaurants based on A grade
        self.boroughs ={
            "BRONX": [],
            "BROOKLYN": [],
            "MANHATTAN": [],
            "QUEENS": [],
            "STATEN ISLAND": []
        }
        self._process_data()

    def _process_data(self):
        for _,record in self.data_frame[self.data_frame["GRADE"] == "A"].iterrows():
            if record["BORO"] != "Missing":

    # Storing relevant info about a restaurant in their respective borough
                restaurant = {
                    "ID": record["CAMIS"],
                    "NAME": record["DBA"],
                    "CUISINE": record["CUISINE DESCRIPTION"],
                    "BUILDING": record["BUILDING"],
                    "STREET": record["STREET"],
                    "BORO": record["BORO"],
                    "ZIPCODE": record["ZIPCODE"],
                    "PHONE": record["PHONE"],
                    "GRADE": record["GRADE"],
                    "SCORE": record["SCORE"]
                }
        
                self.boroughs[record["BORO"]].append(restaurant)

    def sort_by_rating(self):
        for restaurants in self.boroughs.values():
            restaurants.sort(key=lambda x: x["SCORE"])

    def get_dataframe(self):
        return self.data_frame

    def get_boroughs(self):
        return self.boroughs