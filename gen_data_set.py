import pandas as pd
import random
import json
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Define crewRolesList and castingRolesList (copied from React component)
crewRolesList = [
    {"title": "Director", "category": "Core Production"},
    {"title": "Producer", "category": "Core Production"},
    {"title": "Screenwriter", "category": "Core Production"},
    {"title": "Director of Photography", "category": "Core Production"},
    {"title": "Camera Operator", "category": "Core Production"},
    {"title": "Assistant Camera", "category": "Core Production"},
    {"title": "Gaffer", "category": "Core Production"},
    {"title": "Grip", "category": "Core Production"},
    {"title": "Production Designer", "category": "Art and Design"},
    {"title": "Art Director", "category": "Art and Design"},
    {"title": "Set Designer", "category": "Art and Design"},
    {"title": "Costume Designer", "category": "Art and Design"},
    {"title": "Makeup Artist", "category": "Art and Design"},
    {"title": "Hair Stylist", "category": "Art and Design"},
    {"title": "Sound Designer", "category": "Sound and Music"},
    {"title": "Sound Mixer", "category": "Sound and Music"},
    {"title": "Boom Operator", "category": "Sound and Music"},
    {"title": "Editor", "category": "Post-Production"},
    {"title": "Colorist", "category": "Post-Production"},
    {"title": "Production Assistant", "category": "Support Roles"},
    {"title": "Script Supervisor", "category": "Support Roles"},
    {"title": "Location Manager", "category": "Support Roles"},
    {"title": "Casting Director", "category": "Support Roles"},
    {"title": "Special Effects Supervisor", "category": "Additional Roles"},
    {"title": "Visual Effects Supervisor", "category": "Additional Roles"},
    {"title": "Composer", "category": "Sound and Music"},
    {"title": "Music Supervisor", "category": "Sound and Music"},
    {"title": "Unit Production Manager", "category": "Support Roles"},
    {"title": "Assistant Director", "category": "Core Production"},
    {"title": "Second Assistant Director", "category": "Core Production"},
    {"title": "Key Grip", "category": "Core Production"},
    {"title": "Dolly Grip", "category": "Core Production"},
    {"title": "Production Coordinator", "category": "Support Roles"},
    {"title": "Stunt Coordinator", "category": "Additional Roles"},
    {"title": "Choreographer", "category": "Additional Roles"},
    {"title": "Camera Assistant", "category": "Core Production"},
    {"title": "Property Master", "category": "Art and Design"},
    {"title": "Transportation Coordinator", "category": "Support Roles"},
    {"title": "Legal Advisor", "category": "Support Roles"},
    {"title": "Publicist", "category": "Support Roles"},
    {"title": "Social Media Manager", "category": "Support Roles"},
    {"title": "Script Reader", "category": "Support Roles"},
    {"title": "Storyboard Artist", "category": "Art and Design"},
    {"title": "Unit Still Photographer", "category": "Core Production"},
    {"title": "Assistant Editor", "category": "Post-Production"},
    {"title": "Sound Editor", "category": "Post-Production"},
    {"title": "Production Accountant", "category": "Support Roles"},
    {"title": "Production Designer Assistant", "category": "Art and Design"},
    {"title": "Gaffer Assistant", "category": "Core Production"},
    {"title": "Grip Assistant", "category": "Core Production"},
    {"title": "Art Department Assistant", "category": "Art and Design"},
    {"title": "Costume Assistant", "category": "Art and Design"},
    {"title": "Makeup Assistant", "category": "Art and Design"},
    {"title": "Hair Assistant", "category": "Art and Design"},
    {"title": "Special Effects Assistant", "category": "Additional Roles"},
    {"title": "Visual Effects Assistant", "category": "Additional Roles"},
    {"title": "Set Dresser", "category": "Art and Design"},
    {"title": "Set Decoration Assistant", "category": "Art and Design"},
    {"title": "Runner", "category": "Support Roles"},
    {"title": "Driver", "category": "Support Roles"},
    {"title": "Craft Services", "category": "Support Roles"},
    {"title": "Catering Coordinator", "category": "Support Roles"},
    {"title": "Wardrobe Supervisor", "category": "Art and Design"},
    {"title": "Production Sound Mixer", "category": "Sound and Music"},
    {"title": "Sound Re-recording Mixer", "category": "Sound and Music"},
    {"title": "Music Editor", "category": "Sound and Music"},
    {"title": "Dialogue Editor", "category": "Post-Production"},
    {"title": "Foley Artist", "category": "Sound and Music"},
]

castingRolesList = [
    {"title": "Lead Actor", "category": "Main Cast"},
    {"title": "Supporting Actor", "category": "Main Cast"},
    {"title": "Lead Actress", "category": "Main Cast"},
    {"title": "Supporting Actress", "category": "Main Cast"},
    {"title": "Antagonist", "category": "Main Cast"},
    {"title": "Protagonist", "category": "Main Cast"},
    {"title": "Child Actor", "category": "Main Cast"},
    {"title": "Teen Actor", "category": "Main Cast"},
    {"title": "Elderly Actor", "category": "Main Cast"},
    {"title": "Background Actor", "category": "Extras"},
    {"title": "Stand-in", "category": "Extras"},
    {"title": "Photo Double", "category": "Extras"},
    {"title": "Silent Bit Actor", "category": "Extras"},
    {"title": "Featured Extra", "category": "Extras"},
    {"title": "Stunt Performer", "category": "Stunt Roles"},
    {"title": "Stunt Double", "category": "Stunt Roles"},
    {"title": "Fight Coordinator", "category": "Stunt Roles"},
    {"title": "Special Skills Performer", "category": "Stunt Roles"},
    {"title": "Precision Driver", "category": "Stunt Roles"},
    {"title": "Voice Actor", "category": "Voice Roles"},
    {"title": "Narrator", "category": "Voice Roles"},
    {"title": "Dubbing Artist", "category": "Voice Roles"},
    {"title": "Voiceover Artist", "category": "Voice Roles"},
    {"title": "Radio Actor", "category": "Voice Roles"},
    {"title": "Cameo Appearance", "category": "Special Appearances"},
    {"title": "Guest Star", "category": "Special Appearances"},
    {"title": "Host/Presenter", "category": "Special Appearances"},
    {"title": "Celebrity Guest", "category": "Special Appearances"},
    {"title": "Musical Performer", "category": "Special Appearances"},
    {"title": "Commercial Model", "category": "Other Roles"},
    {"title": "Theater Actor", "category": "Other Roles"},
    {"title": "Dancer", "category": "Other Roles"},
    {"title": "Singer", "category": "Other Roles"},
    {"title": "Musician", "category": "Other Roles"},
    {"title": "Magician", "category": "Other Roles"},
    {"title": "Stand-up Comedian", "category": "Other Roles"},
    {"title": "Circus Performer", "category": "Other Roles"},
    {"title": "Puppeteer", "category": "Other Roles"},
    {"title": "Mime Artist", "category": "Other Roles"},
]

# Extract role titles for data generation
CREW_ROLES = [role["title"] for role in crewRolesList]
CASTING_ROLES = [role["title"] for role in castingRolesList]

# Constants
# PROJECT_TYPES = [1, 2, 3, 4, 5]
PROJECT_TYPES = ["Film", "TV", "Theater", "Short Film", "Documentary"]  # Matches backend's project types
PACKAGE_TYPES = ["free", "basic", "premium"]
REVIEW_STATUSES = ["Approved", "Rejected", "Needs Review"]
LOCATIONS = ["Colombo", "Galle", "Kandy", "Nuwara Eliya", "Jaffna", "Trincomalee"]

def generate_synopsis_plagiarism_similarity(review_status):
    """Generate plagiarism score based on target class for balanced distribution."""
    if review_status == "Rejected":
        return round(random.uniform(0.8, 1.0), 2)
    elif review_status == "Needs Review":
        return round(random.uniform(0.5, 0.8), 2)
    else:
        return round(random.uniform(0.0, 0.5), 2)

def generate_dates():
    start_date = fake.date_between(start_date="-1y", end_date="+1y")
    duration_days = random.randint(30, 180)
    end_date = start_date + timedelta(days=duration_days)
    
    rehearsal_date = start_date - timedelta(days=random.randint(7, 21))
    shooting_start = start_date + timedelta(days=random.randint(1, 14))
    
    return {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "production_dates": json.dumps({
            "rehearsal_date": rehearsal_date.strftime("%Y-%m-%d"),
            "shooting_start": shooting_start.strftime("%Y-%m-%d"),
            "duration": f"{duration_days // 30} months"
        })
    }

def generate_production_locations():
    return json.dumps(random.sample(LOCATIONS, k=random.randint(1, 3)))

def generate_crew_roles():
    roles = []
    for _ in range(random.randint(2, 5)):
        role_name = random.choice(CREW_ROLES)
        compensation = random.choice(["Negotiable", f"{random.randint(10, 50)}K LKR"])
        roles.append({"role_name": role_name, "compensation": compensation})
    return json.dumps(roles)

def generate_casting_roles():
    roles = []
    for _ in range(random.randint(3, 6)):
        role_name = random.choice(CASTING_ROLES)
        gender = random.choice(["Male", "Female", "Non-binary"])
        age_range = random.choice(["18-25", "26-35", "36-50", "6-12", "13-17", "50+"])
        compensation = random.choice(["Negotiable", f"{random.randint(15, 40)}K LKR"])
        description = fake.sentence(nb_words=10)
        roles.append({
            "role_name": role_name,
            "gender": gender,
            "age_range": age_range,
            "compensation": compensation,
            "description": description
        })
    return json.dumps(roles)

def generate_review_status():
    """Ensure balanced class distribution for reliable training."""
    return random.choices(
        REVIEW_STATUSES,
        weights=[0.4, 0.3, 0.3],  # Adjust weights for class balance
        k=1
    )[0]

# Generate synthetic data
data = []
for _ in range(10000):  # Generate 10,000 samples for robust splits
    # Basic project details
    project_id = len(data) + 1
    project_type_id = random.choice(PROJECT_TYPES)
    title = fake.catch_phrase()
    description = fake.text(max_nb_chars=200)
    dates = generate_dates()
    synopsis = fake.text(max_nb_chars=150)
    review_status = generate_review_status()
    synopsis_plagiarism_similarity = generate_synopsis_plagiarism_similarity(review_status)
    created_by = fake.user_name()
    package_type_of_user = random.choice(PACKAGE_TYPES)
    
    # Generate features
    production_locations = generate_production_locations()
    crew_roles = generate_crew_roles()
    casting_roles = generate_casting_roles()
    
    # Append to dataset
    data.append({
        "project_id": project_id,
        "project_type_id": project_type_id,
        "title": title,
        "description": description,
        "start_date": dates["start_date"],
        "end_date": dates["end_date"],
        "synopsis": synopsis,
        "synopsis_plagiarism_similarity": synopsis_plagiarism_similarity,
        "created_by": created_by,
        "package_type_of_user": package_type_of_user,
        "production_dates": dates["production_dates"],
        "production_locations": production_locations,
        "crew_roles": crew_roles,
        "casting_roles": casting_roles,
        "review_status": review_status
    })

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv("synthetic_projects_data.csv", index=False)

print(f"Dataset generated with {len(df)} samples.")
print("Class distribution:")
print(df["review_status"].value_counts())
