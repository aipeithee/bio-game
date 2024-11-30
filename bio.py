import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, GREEN, RED = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 36)
BIG_FONT = pygame.font.Font(None, 48)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Biology Quiz Adventure")

# Load background image
background = pygame.image.load("C:/Users/Teacher/Downloads/back.jpg")  
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 

# Questions and answers
questions = [
    {"question": "What is the biological macromolecule made up of proteins that aids in biochemical processes by hastening the rate of reaction?",
     "options": ["Lipids", "Carbohydrates", "Enzymes", "Nucleic Acids"], "answer": "Enzymes"},
    {"question": "In the known and recorded history, who is the first person to isolate enzyme from malt extract?",
     "options": ["Louis Pasteur", "Alexander Fleming", "Anselme Payen", "Robert Koch"], "answer": "Anselme Payen"},
    {"question": "After you were transported into the future, you noticed cellular processes are slower. What could be the reason?",
     "options": ["Too much ATP", "Lack of enzymes", "Mutation", "Excess oxygen"], "answer": "Lack of enzymes"},
    {"question": "Which of the following will happen if there is no enzyme in your body?",
     "options": ["Faster muscle movement", "Hot but slow muscle movement", "Normal cellular processes", "Overproduction of ATP"], "answer": "Hot but slow muscle movement"},
    {"question": "Which of the following will happen if you keep increasing the temperature beyond the optimal temperature of an enzyme?",
     "options": ["Enzyme speeds up", "Enzyme denatures", "Enzyme works better", "Enzyme multiplies"], "answer": "Enzyme denatures"},
    {"question": "Which of the following made-up chemical names is an enzyme?",
     "options": ["Camarinase", "Waterase", "Oxyper", "Energine"], "answer": "Camarinase"},
    {"question": "Goease is an enzyme with an optimal pH of 5. What happens if you increase the pH?",
     "options": ["Reaction increases", "Reaction decreases and stops", "No effect", "Enzyme multiplies"], "answer": "Reaction decreases and stops"},
    {"question": "How does an enzyme speed up the rate of chemical reactions?",
     "options": ["It increases temperature", "It lowers activation energy", "It consumes ATP", "It adds oxygen"], "answer": "It lowers activation energy"},
    {"question": "What is the importance of coupled reactions in the body?",
     "options": ["It conserves oxygen", "It links energy-producing and consuming reactions", "It increases pH", "It stores water"], "answer": "It links energy-producing and consuming reactions"},
    {"question": "Which of the following scenarios represent an exergonic reaction?",
     "options": ["Heat from clapping hands", "ATP synthesis", "Absorbing light", "Protein synthesis"], "answer": "Heat from clapping hands"},
    {"question": "What is the reason why dissolving synthetic fertilizer feels cold?",
     "options": ["It releases heat", "It consumes energy", "It stores ATP", "It absorbs oxygen"], "answer": "It consumes energy"},
    {"question": "What is the energy currency of the body?",
     "options": ["ATP", "Glucose", "NADPH", "Oxygen"], "answer": "ATP"},
    {"question": "What type of reaction breaks down complex molecules into simpler ones, releasing energy?",
     "options": ["Anabolism", "Synthesis", "Catabolism", "Respiration"], "answer": "Catabolism"},
    {"question": "Which reaction does not belong to the group of anabolic processes?",
     "options": ["Protein synthesis", "Photosynthesis", "Digestion", "DNA synthesis"], "answer": "Digestion"},
    {"question": "Why can't the body store all energy from food as ATP for a long time?",
     "options": ["It would overload mitochondria", "It would overheat the body", "ATP degrades quickly", "ATP becomes toxic"], "answer": "ATP degrades quickly"},
    {"question": "Why does a living person feel hot compared to a deceased one?",
     "options": ["Excess oxygen", "Energy released by cell respiration", "Muscle activity", "Decomposing cells"], "answer": "Energy released by cell respiration"},
    {"question": "What organelle in plants acts like a tiny solar panel?",
     "options": ["Mitochondria", "Chloroplast", "Ribosome", "Vacuole"], "answer": "Chloroplast"},
    {"question": "What process allows beings on another planet to synthesize food using sunlight?",
     "options": ["Respiration", "Photosynthesis", "Glycolysis", "Fermentation"], "answer": "Photosynthesis"},
    {"question": "Who coined the term chlorophyll?",
     "options": ["Anselme Payen", "Caventou and Pelletier", "Louis Pasteur", "Alexander Fleming"], "answer": "Caventou and Pelletier"},
    {"question": "What is the primary pigment for photosynthesis?",
     "options": ["Anthocyanins", "Xanthophylls", "Carotenoids", "Chlorophyll"], "answer": "Chlorophyll"}
]

# Game variables
bio_points = 0
streak = 0
current_question = 0
game_running = True

# Function to display text on the screen

def draw_text(text, font, color, x, y, center=False):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y)) if center else render.get_rect(topleft=(x, y))
    screen.blit(render, rect)

# Function to display a question and options
def display_question(q):
    global streak
    screen.fill(WHITE)
    
    # Display question
    draw_text(f"Question {current_question + 1}:", FONT, BLACK, 20, 20)
    draw_text(q["question"], FONT, BLACK, 20, 80)

    # Display options
    for i, option in enumerate(q["options"]):
        draw_text(f"{chr(97 + i)}. {option}", FONT, BLACK, 20, 160 + i * 50)

    # Display current points and streak
    draw_text(f"Points: {bio_points}", FONT, GREEN, WIDTH - 200, 20)
    draw_text(f"Streak: {streak}", FONT, GREEN, WIDTH - 200, 60)
    pygame.display.flip()

# Function to handle user input and check the answer
def handle_answer(q, answer_index):
    global bio_points, streak
    if q["options"][answer_index] == q["answer"]:
        bio_points += 10
        streak += 1
        if streak % 5 == 0:
            bio_points += 10
    else:
        bio_points -= 5
        streak = 0

# Main game loop
def main():
    global current_question, game_running

    while game_running:
        if current_question < len(questions):
            display_question(questions[current_question])
        else:
            # End of game
            screen.fill(WHITE)
            draw_text("Game Over!", BIG_FONT, BLACK, WIDTH // 2, HEIGHT // 3, center=True)
            draw_text(f"Your total points: {bio_points}", FONT, GREEN, WIDTH // 2, HEIGHT // 2, center=True)
            pygame.display.flip()
            pygame.time.wait(3000)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    handle_answer(questions[current_question], 0)
                    current_question += 1
                elif event.key == pygame.K_b:
                    handle_answer(questions[current_question], 1)
                    current_question += 1
                elif event.key == pygame.K_c:
                    handle_answer(questions[current_question], 2)
                    current_question += 1
                elif event.key == pygame.K_d:
                    handle_answer(questions[current_question], 3)
                    current_question += 1

    pygame.quit()
def draw_wrapped_text(text, font, color, x, y, max_width):
    """Draw text that wraps if it's too long."""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    for i, line in enumerate(lines):
        render = font.render(line, True, color)
        screen.blit(render, (x, y + i * font.get_height()))

# Modify display_question to use draw_wrapped_text for the question
def display_question(q):
    global streak
    screen.fill(WHITE)
    
    # Display question
    draw_text(f"Question {current_question + 1}:", FONT, BLACK, 20, 20)
    draw_wrapped_text(q["question"], FONT, BLACK, 20, 80, WIDTH - 40)

    # Display options
    for i, option in enumerate(q["options"]):
        draw_text(f"{chr(97 + i)}. {option}", FONT, BLACK, 20, 200 + i * 50)

    # Display current points and streak
    draw_text(f"Points: {bio_points}", FONT, GREEN, WIDTH - 200, 20)
    draw_text(f"Streak: {streak}", FONT, GREEN, WIDTH - 200, 60)
    pygame.display.flip()
    
  


# Shuffle questions and start the game
random.shuffle(questions)
main()
