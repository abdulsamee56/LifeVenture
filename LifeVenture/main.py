import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LifeVenture")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 24)  # Smaller font size
title_font = pygame.font.SysFont(None, 36)  # Larger font size for title

# Load background image
background_image = pygame.image.load("img/cloudbackground.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load title image and scale it down
title_image = pygame.image.load("img/lifeventure.png")
title_image = pygame.transform.scale(title_image,
                                     (int(title_image.get_width() * 0.5), int(title_image.get_height() * 0.5)))

# List of random male names
male_names = ["Jack", "John", "Michael", "William", "James", "Daniel", "Matthew", "David", "Joseph", "Andrew",
              "Benjamin", "Christopher", "Elijah", "Gabriel", "Henry"]

# List of random female names
female_names = ["Emily", "Emma", "Olivia", "Sophia", "Isabella", "Ava", "Mia", "Abigail", "Emily", "Charlotte",
                "Amelia", "Evelyn", "Grace", "Hannah", "Lily"]

# List of random birth locations
birth_locations = ["New York, USA", "London, UK", "Paris, France", "Tokyo, Japan", "Sydney, Australia",
                   "Toronto, Canada", "Berlin, Germany", "Rome, Italy", "Moscow, Russia", "Beijing, China"]

# Character information
gender = None
name = None
birth_location = None
birthday = None
mother_name = None
mother_age = None
father_name = None
father_age = None
age = 0

# Game state
STATE_GENDER_SELECTION = 0
STATE_CHARACTER_INFO = 1
game_state = STATE_GENDER_SELECTION


# Function to generate character information
def generate_character_info():
    global name, birth_location, birthday, mother_name, mother_age, father_name, father_age
    # Generate random name based on selected gender
    if gender == "Male":
        name = random.choice(male_names)
        mother_name = random.choice(female_names)  # Randomly select mother's name from female_names
        father_name = random.choice(male_names)    # Randomly select father's name from male_names
    else:
        name = random.choice(female_names)
        mother_name = random.choice(female_names)  # Randomly select mother's name from female_names
        father_name = random.choice(male_names)    # Randomly select father's name from male_names
    # Other character info generation...
    birth_location = random.choice(birth_locations)  # You can randomize this too
    birthday = "01/01/2000"  # You can randomize this too

    mother_age = random.randint(18, 100)  # Mother should be at least 18
    father_age = random.randint(mother_age + 1, 100)  # Randomly select father's age

# Function to draw character information
def draw_character_info():
    info = [
        f"Gender: {gender}",
        f"Name: {name}",
        f"Birth Location: {birth_location}",
        f"Birthday: {birthday}",
        f"Mother: {mother_name} (Age: {mother_age})",
        f"Father: {father_name} (Age: {father_age})",
        f"Age: {age} years"
    ]
    for i, line in enumerate(info):
        text_surface = font.render(line, True, BLACK)
        screen.blit(text_surface, (10, 10 + i * 30))


# Function to draw gender selection buttons
def draw_gender_selection():
    male_button = pygame.Rect((WIDTH - 200) / 2, 250, 100, 50)
    female_button = pygame.Rect((WIDTH + 20) / 2, 250, 100, 50)
    pygame.draw.rect(screen, BLUE, male_button)  # Blue for male button
    pygame.draw.rect(screen, RED, female_button)  # Red for female button
    male_text = font.render("Male", True, WHITE)  # Text color for male button
    female_text = font.render("Female", True, WHITE)  # Text color for female button
    screen.blit(male_text, (male_button.centerx - male_text.get_width() / 2, 265))
    screen.blit(female_text, (female_button.centerx - female_text.get_width() / 2, 265))


# Function to draw age increase button
def draw_age_increase_button():
    pygame.draw.rect(screen, BLUE, (WIDTH - 150, HEIGHT - 100, 100, 50))  # Blue button for age increase
    age_text = font.render("+1 Age", True, WHITE)
    screen.blit(age_text, (WIDTH - 125, HEIGHT - 85))


# Main game loop
running = True
while running:
    screen.fill(WHITE)

    if game_state == STATE_GENDER_SELECTION:
        screen.blit(background_image, (0, 0))  # Draw background image for gender selection screen
        # Draw title image
        screen.blit(title_image, (WIDTH / 2 - title_image.get_width() / 2, 50))
        # Draw "Choose Your Gender" text
        choose_gender_text = font.render("Choose Your Gender", True, BLACK)
        screen.blit(choose_gender_text, (WIDTH / 2 - choose_gender_text.get_width() / 2, 200))
        # Draw gender selection buttons
        draw_gender_selection()
    elif game_state == STATE_CHARACTER_INFO:
        # Draw character information
        draw_character_info()
        # Draw age increase button
        draw_age_increase_button()

    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game_state == STATE_GENDER_SELECTION:
                if (WIDTH - 200) / 2 <= mouse_pos[0] <= (WIDTH - 200) / 2 + 100 and 250 <= mouse_pos[1] <= 300:
                    # Male button clicked
                    gender = "Male"
                    generate_character_info()
                    game_state = STATE_CHARACTER_INFO
                elif (WIDTH + 20) / 2 <= mouse_pos[0] <= (WIDTH + 20) / 2 + 100 and 250 <= mouse_pos[1] <= 300:
                    # Female button clicked
                    gender = "Female"
                    generate_character_info()
                    game_state = STATE_CHARACTER_INFO
            elif game_state == STATE_CHARACTER_INFO:
                # Check if age increase button is clicked
                if WIDTH - 150 <= mouse_pos[0] <= WIDTH - 50 and HEIGHT - 100 <= mouse_pos[1] <= HEIGHT - 50:
                    # Increase character's age by 1
                    age += 1

pygame.quit()
