# # import pandas as pd
# # import random
# # from faker import Faker
# # import json
# # from datetime import timedelta

# # # Initialize Faker
# # fake = Faker()

# # def generate_random_production_dates():
# #     start = fake.date_between(start_date="-1y", end_date="today")
# #     end = start + timedelta(days=random.randint(30, 180))  # Random end date 1 to 6 months later
# #     return {"start": str(start), "end": str(end)}

# # def generate_random_locations():
# #     return [fake.city() for _ in range(random.randint(1, 3))]

# # def generate_random_roles(role_type, count=3):
# #     return {role_type: fake.name() for _ in range(count)}

# # # Generate synthetic dataset
# # def generate_dataset(num_records=100):
# #     data = []
# #     for _ in range(num_records):
# #         title = fake.sentence(nb_words=4)
# #         description = fake.paragraph(nb_sentences=3)
# #         start_date = fake.date_between(start_date="-1y", end_date="today")
# #         end_date = start_date + timedelta(days=random.randint(30, 180))
# #         synopsis = fake.text(max_nb_chars=200)
# #         production_dates = json.dumps(generate_random_production_dates())
# #         production_locations = json.dumps(generate_random_locations())
# #         crew_roles = json.dumps(generate_random_roles("Crew"))
# #         casting_roles = json.dumps(generate_random_roles("Casting"))
# #         review_status = random.choice(["Approved", "Pending"])

# #         data.append({
# #             "Title": title,
# #             "Description": description,
# #             "StartDate": str(start_date),
# #             "EndDate": str(end_date),
# #             "Synopsis": synopsis,
# #             "ProductionDates": production_dates,
# #             "ProductionLocations": production_locations,
# #             "CrewRoles": crew_roles,
# #             "CastingRoles": casting_roles,
# #             "ReviewStatus": review_status
# #         })
    
# #     return pd.DataFrame(data)

# # # Generate and save dataset
# # if __name__ == "__main__":
# #     num_records = 500  # Adjust as needed
# #     dataset = generate_dataset(num_records)
# #     dataset.to_csv("projects_dataset.csv", index=False)
# #     print(f"Dataset with {num_records} records saved as 'projects_dataset.csv'.")

# import pandas as pd
# import random
# from faker import Faker
# import json
# from datetime import timedelta

# # Initialize Faker
# fake = Faker()

# # Function to generate a random list of crew roles
# def generate_random_crew_roles(count=5):
#     crew_roles = [
#         "Director", "Producer", "Cinematographer", "Editor", "Sound Designer", 
#         "Composer", "Costume Designer", "Production Designer", "Script Supervisor", "Assistant Director"
#     ]
#     return random.sample(crew_roles, k=min(count, len(crew_roles)))

# # Function to generate a random list of casting roles
# def generate_random_casting_roles(count=5):
#     casting_roles = [
#         "Lead Actor", "Supporting Actor", "Villain", "Extra", "Cameo",
#         "Child Actor", "Love Interest", "Sidekick", "Narrator", "Antagonist"
#     ]
#     return random.sample(casting_roles, k=min(count, len(casting_roles)))

# # Generate a random production date range
# def generate_random_production_dates():
#     start = fake.date_between(start_date="-1y", end_date="today")
#     end = start + timedelta(days=random.randint(30, 180))  # Random end date 1 to 6 months later
#     return {"start": str(start), "end": str(end)}

# # Generate a random location list
# def generate_random_locations():
#     return [fake.city() for _ in range(random.randint(1, 3))]

# # Generate a synthetic dataset
# def generate_dataset(num_records=100):
#     data = []
#     for _ in range(num_records):
#         title = fake.sentence(nb_words=4)
#         description = fake.text(max_nb_chars=500)  # General description of the film
#         synopsis = f"{title} is a {fake.word()} film that follows {fake.name()} as they encounter {fake.word()} challenges in a {fake.word()} world. The story unfolds as {fake.sentence()}"
#         start_date = fake.date_between(start_date="-1y", end_date="today")
#         end_date = start_date + timedelta(days=random.randint(30, 180))
#         production_dates = json.dumps(generate_random_production_dates())
#         production_locations = json.dumps(generate_random_locations())
#         crew_roles = json.dumps(generate_random_crew_roles(count=5))
#         casting_roles = json.dumps(generate_random_casting_roles(count=5))
#         review_status = random.choice(["Approved", "Pending"])

#         data.append({
#             "Title": title,
#             "Description": description,
#             "Synopsis": synopsis,
#             "StartDate": str(start_date),
#             "EndDate": str(end_date),
#             "ProductionDates": production_dates,
#             "ProductionLocations": production_locations,
#             "CrewRoles": crew_roles,
#             "CastingRoles": casting_roles,
#             "ReviewStatus": review_status
#         })
    
#     return pd.DataFrame(data)

# # Generate and save dataset
# if __name__ == "__main__":
#     num_records = 500  # Adjust as needed
#     dataset = generate_dataset(num_records)
#     dataset.to_csv("projects_dataset.csv", index=False)
#     print(f"Dataset with {num_records} records saved as 'projects_dataset.csv'.")


import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_dataset(num_records=100):
    data = []
    for _ in range(num_records):
        description = fake.paragraph(nb_sentences=3)
        synopsis = fake.paragraph(nb_sentences=2)
        review_status = random.choice(["Approved", "Rejected", "Pending"])
        data.append({
            "description": description,
            "synopsis": synopsis,
            "review_status": review_status
        })
    return pd.DataFrame(data)

dataset = generate_dataset(100)
dataset.to_csv('projects_dataset.csv', index=False)
print("Dataset saved to 'projects_dataset.csv'.")
