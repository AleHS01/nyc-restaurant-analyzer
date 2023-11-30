import pandas as pd


class RestaurantData:
    def __init__(self, file_path):
        # Load data from the specified CSV file
        self.data_frame = pd.read_csv(file_path)

        # Process the DataFrame to get boroughs and their restaurants based on A grade
        self.boroughs = {
            "BRONX": [],
            "BROOKLYN": [],
            "MANHATTAN": [],
            "QUEENS": [],
            "STATEN ISLAND": [],
        }
        self.sort_by_rating()
        self._process_data()

    def _process_data(self):
        camis_set = set()  # a set of camis/id to avoid restaurant repetition

        for _, record in self.data_frame[self.data_frame["GRADE"] == "A"].iterrows():
            if record["BORO"] != "Missing":
                camis = record["CAMIS"]
                if camis not in camis_set:
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
                        "SCORE": record["SCORE"],
                    }

                    self.boroughs[record["BORO"]].append(restaurant)
                    camis_set.add(camis)

    def sort_by_rating(self):
        self.data_frame = self.data_frame.sort_values(
            by=["SCORE", "GRADE"], ascending=[True, True]
        )

    def get_dataframe(self):
        return self.data_frame

    def get_boroughs(self):
        return self.boroughs
