import pygame
import random
import time

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

outcome_display_time = None
pause_duration = 2  # 2 seconds pause duration



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
STATE_AGE_5_EVENT = 2
STATE_AGE_10_EVENT = 3
STATE_AGE_13_EVENT = 4
STATE_AGE_16_EVENT = 5
STATE_AGE_18_EVENT = 6
STATE_AGE_20_EVENT = 7
STATE_AGE_21_EVENT = 8
STATE_AGE_22_EVENT = 9
STATE_AGE_23_EVENT = 10
STATE_AGE_24_EVENT = 11
STATE_GAME_OVER = 12
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
    
# Function to draw choice buttons with text
def draw_choice_button(text, x, y, width, height, choice_rect):
    pygame.draw.rect(screen, BLUE, choice_rect)
    choice_text = font.render(text, True, WHITE)
    screen.blit(choice_text, (x + (width - choice_text.get_width()) / 2, y + (height - choice_text.get_height()) / 2))

bad_choices_count = 0

# Age 5 Event: Your character starts school.
# Choices:
# - Attend school enthusiastically.
# - Feel nervous about starting school.
def generate_age_5_event():
    event_description = "You start school!"
    return event_description

def draw_age_5_event():
    event_description = generate_age_5_event()
    screen.blit(font.render(event_description, True, BLACK), (10, 100))
    # Draw choice buttons
    choice1_rect = pygame.Rect(50, 300, 200, 50)
    choice2_rect = pygame.Rect(50, 400, 200, 50)
    draw_choice_button("Attend school enthusiastically.", 50, 300, 200, 50, choice1_rect)
    draw_choice_button("Feel nervous about starting school.", 50, 400, 200, 50, choice2_rect)


# Age 10 Event: Your character discovers a hidden treasure in the backyard.
# Choices:
# - Keep the treasure a secret.
# - Share the treasure with friends.
def generate_age_10_event():
    event_description = "You discover a hidden treasure in the backyard!"
    return event_description

def draw_age_10_event():
    event_description = generate_age_10_event()
    screen.blit(font.render(event_description, True, BLACK), (10, 100))


# Age 13 Event: Your character wins a local talent show.
# Choices:
# - Pursue a career in performing arts.
# - Keep it as a hobby and focus on studies.
def generate_age_13_event():
    event_description = "You win a local talent show!"
    return event_description

def draw_age_13_event():
    event_description = generate_age_13_event()
    screen.blit(font.render(event_description, True, BLACK), (10, 100))


# Age 16 Event: Your character gets their first job at a local cafe.
# Choices:
# - Save money for future goals.
# - Spend money on leisure activities.
def generate_age_16_event():
    event_description = "You get your first job at a local cafe!"
    return event_description

def draw_age_16_event():
    event_description = generate_age_16_event()
    screen.blit(font.render(event_description, True, BLACK), (10, 100))


# Age 18 Event: Your character graduates from high school.
# Choices:
# - Attend college/university.
# - Pursue other opportunities (e.g., travel, work).
def generate_age_18_event():
    event_description = "You graduate from high school!"
    return event_description

def draw_age_18_event():
    event_description = generate_age_18_event()
    screen.blit(font.render(event_description, True, BLACK), (10, 100))

def handle_age_5_choice_1():
    global game_state
    # Display outcome of choice 1
    outcome_text = "You attend school enthusiastically and make many new friends!"
    outcome_surface = font.render(outcome_text, True, BLACK)
    screen.blit(outcome_surface, (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 2 for age 5 event
def handle_age_5_choice_2():
    global game_state, bad_choices_count
    # Display outcome of choice 2
    bad_choices_count += 1
    outcome_text = "You feel nervous about starting school and fail to make any friends"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 1 for age 10 event
def handle_age_10_choice_1():
    global game_state
    # Display outcome of choice 1
    outcome_text = "You decide to keep the treasure a secret for yourself!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 2 for age 10 event
def handle_age_10_choice_2():
    global game_state, bad_choices_count
    # Display outcome of choice 2
    bad_choices_count += 1
    outcome_text = "You share the treasure with your friends and have a fun treasure hunt together!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 1 for age 13 event
def handle_age_13_choice_1():
    global game_state
    # Display outcome of choice 1
    outcome_text = "You pursue a career in performing arts and become a successful actor/actress!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 2 for age 13 event
def handle_age_13_choice_2():
    global game_state, bad_choices_count
    # Display outcome of choice 2
    bad_choices_count += 1
    outcome_text = "You keep performing arts as a hobby while focusing on your studies and achieve academic success!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 1 for age 16 event
def handle_age_16_choice_1():
    global game_state
    # Display outcome of choice 1
    outcome_text = "You save money for future goals and learn valuable financial management skills!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 2 for age 16 event
def handle_age_16_choice_2():
    global game_state
    # Display outcome of choice 2
    outcome_text = "You spend money on leisure activities and enjoy your teenage years to the fullest!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 1 for age 18 event
def handle_age_18_choice_1():
    global game_state
    # Display outcome of choice 1
    outcome_text = "You attend college/university and pursue higher education to achieve your career goals!"
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to handle choice 2 for age 18 event
def handle_age_18_choice_2():
    global game_state, bad_choices_count
    # Display outcome of choice 2
    bad_choices_count += 1
    outcome_text = "You decide to pursue other opportunities such as traveling or exploring different career paths, but struggle to find stability in your life."
    screen.blit(font.render(outcome_text, True, BLACK), (10, 200))
    # Return to main information screen
    game_state = STATE_CHARACTER_INFO

# Function to display ending based on the number of bad choices
def display_ending():
    global bad_choices_count
    if bad_choices_count == 0:
        ending_text = "Congratulations! You have lived a successful and happy life!"
    elif bad_choices_count < 4:
        ending_text = "You lived a normal life with average pay, always wondering what could have been..."
    else:
        ending_text = "You made all the wrong choices and ended up homeless, living off the streets."
    screen.blit(font.render(ending_text, True, BLACK), (10, 200))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    if game_state == STATE_GENDER_SELECTION:
        screen.blit(background_image, (0, 0))  # Draw background image for gender selection screen
        screen.blit(title_image, (WIDTH / 2 - title_image.get_width() / 2, 50))  # Draw title image
        choose_gender_text = font.render("Choose Your Gender", True, BLACK)
        screen.blit(choose_gender_text, (WIDTH / 2 - choose_gender_text.get_width() / 2, 200))
        draw_gender_selection()
    elif game_state == STATE_CHARACTER_INFO:
        draw_character_info()
        draw_age_increase_button()
    elif game_state == STATE_AGE_5_EVENT:
        draw_age_5_event()
        # Handle choices for age 5 event
        choice1_rect = pygame.Rect(50, 300, 200, 50)
        choice2_rect = pygame.Rect(50, 400, 200, 50)
        pygame.draw.rect(screen, BLUE, choice1_rect)
        pygame.draw.rect(screen, RED, choice2_rect)
        choice1_text = font.render("Attend school enthusiastically.", True, WHITE)
        choice2_text = font.render("Feel nervous about starting school.", True, WHITE)
        screen.blit(choice1_text, (60, 315))
        screen.blit(choice2_text, (60, 415))
    elif game_state == STATE_AGE_10_EVENT:
        draw_age_10_event()
        # Handle choices for age 10 event
        choice1_rect = pygame.Rect(50, 300, 200, 50)
        choice2_rect = pygame.Rect(50, 400, 200, 50)
        pygame.draw.rect(screen, BLUE, choice1_rect)
        pygame.draw.rect(screen, RED, choice2_rect)
        choice1_text = font.render("Keep the treasure a secret.", True, WHITE)
        choice2_text = font.render("Share the treasure with friends.", True, WHITE)
        screen.blit(choice1_text, (60, 315))
        screen.blit(choice2_text, (60, 415))
    elif game_state == STATE_AGE_13_EVENT:
        draw_age_13_event()
        # Handle choices for age 13 event
        choice1_rect = pygame.Rect(50, 300, 200, 50)
        choice2_rect = pygame.Rect(50, 400, 200, 50)
        pygame.draw.rect(screen, BLUE, choice1_rect)
        pygame.draw.rect(screen, RED, choice2_rect)
        choice1_text = font.render("Pursue a career in performing arts.", True, WHITE)
        choice2_text = font.render("Keep it as a hobby and focus on studies.", True, WHITE)
        screen.blit(choice1_text, (60, 315))
        screen.blit(choice2_text, (60, 415))
    elif game_state == STATE_AGE_16_EVENT:
        draw_age_16_event()
        # Handle choices for age 16 event
        choice1_rect = pygame.Rect(50, 300, 200, 50)
        choice2_rect = pygame.Rect(50, 400, 200, 50)
        pygame.draw.rect(screen, BLUE, choice1_rect)
        pygame.draw.rect(screen, RED, choice2_rect)
        choice1_text = font.render("Save money for future goals.", True, WHITE)
        choice2_text = font.render("Spend money on leisure activities.", True, WHITE)
        screen.blit(choice1_text, (60, 315))
        screen.blit(choice2_text, (60, 415))
    elif game_state == STATE_AGE_18_EVENT:
        draw_age_18_event()
        # Handle choices for age 18 event
        choice1_rect = pygame.Rect(50, 300, 200, 50)
        choice2_rect = pygame.Rect(50, 400, 200, 50)
        pygame.draw.rect(screen, BLUE, choice1_rect)
        pygame.draw.rect(screen, RED, choice2_rect)
        choice1_text = font.render("Attend college/university.", True, WHITE)
        choice2_text = font.render("Pursue other opportunities.", True, WHITE)
        screen.blit(choice1_text, (60, 315))
        screen.blit(choice2_text, (60, 415))
    elif game_state == STATE_GAME_OVER:
        display_ending()
    elif age == 19:
        display_ending()  # Display ending when the user becomes 19 years old

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game_state == STATE_GENDER_SELECTION:
                if (WIDTH - 200) / 2 <= mouse_pos[0] <= (WIDTH - 200) / 2 + 100 and 250 <= mouse_pos[1] <= 300:
                    gender = "Male"
                    generate_character_info()
                    game_state = STATE_CHARACTER_INFO
                elif (WIDTH + 20) / 2 <= mouse_pos[0] <= (WIDTH + 20) / 2 + 100 and 250 <= mouse_pos[1] <= 300:
                    gender = "Female"
                    generate_character_info()
                    game_state = STATE_CHARACTER_INFO
            elif game_state == STATE_CHARACTER_INFO:
                if WIDTH - 150 <= mouse_pos[0] <= WIDTH - 50 and HEIGHT - 100 <= mouse_pos[1] <= HEIGHT - 50:
                    age += 1
                    # Check age and transition to the corresponding event state
                    if age == 5:
                        game_state = STATE_AGE_5_EVENT
                    elif age == 10:
                        game_state = STATE_AGE_10_EVENT
                    elif age == 13:
                        game_state = STATE_AGE_13_EVENT
                    elif age == 16:
                        game_state = STATE_AGE_16_EVENT
                    elif age == 18:
                        game_state = STATE_AGE_18_EVENT
                    elif age == 19:
                        game_state = STATE_GAME_OVER
            # Handle choice selection for events
            elif game_state == STATE_AGE_5_EVENT:
                # Age 5 event screen
                # ...

                # Handle choices for age 5 event
                if choice1_rect.collidepoint(mouse_pos):
                    handle_age_5_choice_1()
                elif choice2_rect.collidepoint(mouse_pos):
                    handle_age_5_choice_2()

            elif game_state == STATE_AGE_10_EVENT:
                # Age 10 event screen
                # ...

                # Handle choices for age 10 event
                if choice1_rect.collidepoint(mouse_pos):
                    handle_age_10_choice_1()
                elif choice2_rect.collidepoint(mouse_pos):
                    handle_age_10_choice_2()

            elif game_state == STATE_AGE_13_EVENT:
                # Age 13 event screen
                # ...

                # Handle choices for age 13 event
                if choice1_rect.collidepoint(mouse_pos):
                    handle_age_13_choice_1()
                elif choice2_rect.collidepoint(mouse_pos):
                    handle_age_13_choice_2()

            elif game_state == STATE_AGE_16_EVENT:
                # Age 16 event screen
                # ...

                # Handle choices for age 16 event
                if choice1_rect.collidepoint(mouse_pos):
                    handle_age_16_choice_1()
                elif choice2_rect.collidepoint(mouse_pos):
                    handle_age_16_choice_2()

            elif game_state == STATE_AGE_18_EVENT:
                # Age 18 event screen
                # ...

                # Handle choices for age 18 event
                if choice1_rect.collidepoint(mouse_pos):
                    handle_age_18_choice_1()
                elif choice2_rect.collidepoint(mouse_pos):
                    handle_age_18_choice_2()

pygame.quit()

