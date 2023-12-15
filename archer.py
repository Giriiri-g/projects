import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Archer Game")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the archer
archer_width = 50
archer_height = 100
archer_x = WIDTH // 2 - archer_width // 2
archer_y = HEIGHT - archer_height
archer_speed = 5
fire_delay = 150  # Delay between consecutive arrow shots in milliseconds
last_shot_time = 0  # Time of the last arrow shot

# Set up the arrow
arrow_width = 10
arrow_height = 30
arrow_speed = 10
arrows = []

# Set up the targets
targets = []
num_targets = 5
target_width = 50
target_height = 50
target_speed = 1

for _ in range(num_targets):
    target_x = random.randint(0, WIDTH - target_width)
    target_y = random.randint(50, HEIGHT - target_height - 50)
    targets.append({"x": target_x, "y": target_y, "speed": target_speed})

# Set up the score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

# Set up game states
game_over = False
game_start = False
timer = 60
start_ticks = 0

# Set up restart button
button_width = 200
button_height = 50
button_x = WIDTH // 2 - button_width // 2
button_y = HEIGHT // 2 + 50

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_start and not game_over:
                    game_start = True
                    start_ticks = pygame.time.get_ticks()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if game_start and not game_over:
                    last_shot_time = 0  # Reset the last shot time when the spacebar is released

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (
                    button_x <= mouse_x <= button_x + button_width
                    and button_y <= mouse_y <= button_y + button_height
                ):
                    # Restart the game
                    game_over = False
                    game_start = False
                    score = 0
                    targets.clear()
                    arrows.clear()
                    start_ticks = 0

                    for _ in range(num_targets):
                        target_x = random.randint(0, WIDTH - target_width)
                        target_y = random.randint(50, HEIGHT - target_height - 50)
                        targets.append({"x": target_x, "y": target_y, "speed": target_speed})

    # Handle archer movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and archer_x > 0:
        archer_x -= archer_speed
    if keys[pygame.K_RIGHT] and archer_x < WIDTH - archer_width:
        archer_x += archer_speed

    # Handle arrow firing
    if game_start and not game_over and keys[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - last_shot_time > fire_delay:
            arrow_x = archer_x + archer_width // 2 - arrow_width // 2
            arrow_y = archer_y
            arrows.append({"x": arrow_x, "y": arrow_y})
            last_shot_time = current_time

    # Update arrow positions
    for arrow in arrows:
        arrow["y"] -= arrow_speed
        if arrow["y"] < 0:
            arrows.remove(arrow)

    # Update target positions and generate new targets
    if game_start and not game_over:
        for target in targets:
            target["y"] += target["speed"]
            if target["y"] > HEIGHT:
                targets.remove(target)
                score -= 1
                if len(targets) < num_targets:
                    new_target_x = random.randint(0, WIDTH - target_width)
                    new_target_y = random.randint(-target_height, -target_height // 2)
                    targets.append({"x": new_target_x, "y": new_target_y, "speed": target_speed})

    # Check for collision between archer and targets
    for target in targets:
        if (
            archer_x < target["x"] + target_width
            and archer_x + archer_width > target["x"]
            and archer_y < target["y"] + target_height
            and archer_y + archer_height > target["y"]
        ):
            game_over = True

    # Check for collision between arrow and target
    for target in targets:
        for arrow in arrows:
            if (
                arrow["x"] + arrow_width >= target["x"]
                and arrow["x"] <= target["x"] + target_width
                and arrow["y"] <= target["y"] + target_height
            ):
                score += 1
                arrows.remove(arrow)
                targets.remove(target)
                new_target_x = random.randint(0, WIDTH - target_width)
                new_target_y = random.randint(-target_height, -target_height // 2)
                targets.append({"x": new_target_x, "y": new_target_y, "speed": target_speed})
                break

    # Check if targets reach the floor
    for target in targets:
        if target["y"] >= HEIGHT:
            targets.remove(target)
            score -= 1
            if len(targets) < num_targets:
                new_target_x = random.randint(0, WIDTH - target_width)
                new_target_y = random.randint(-target_height, -target_height // 2)
                targets.append({"x": new_target_x, "y": new_target_y, "speed": target_speed})

    # Update the screen
    window.fill(WHITE)

    # Draw archer
    pygame.draw.rect(window, RED, (archer_x, archer_y, archer_width, archer_height))

    if game_start and not game_over:
        # Draw targets
        for target in targets:
            pygame.draw.rect(window, RED, (target["x"], target["y"], target_width, target_height))

        # Draw arrows
        for arrow in arrows:
            pygame.draw.rect(window, RED, (arrow["x"], arrow["y"], arrow_width, arrow_height))

        # Update timer
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds >= timer:
            game_over = True

        # Draw timer
        time_text = font.render("Time: " + str(timer - seconds), True, RED)
        window.blit(time_text, (10, 10))

        # Draw score
        score_text = font.render("Score: " + str(score), True, RED)
        window.blit(score_text, (10, 50))

    if not game_start:
        # Draw start message
        start_text = font.render("Press SPACE to start", True, RED)
        window.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))

    if game_over:
        # Draw game over message
        game_over_text = font.render("Game Over", True, RED)
        window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        final_score_text = font.render("Final Score: " + str(score), True, RED)
        window.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + final_score_text.get_height()))

        # Draw restart button
        pygame.draw.rect(window, RED, (button_x, button_y, button_width, button_height))
        restart_text = font.render("Restart", True, WHITE)
        window.blit(restart_text, (button_x + button_width // 2 - restart_text.get_width() // 2, button_y + button_height // 2 - restart_text.get_height() // 2))

    pygame.display.update()

    # Add a delay to slow down the game update
    pygame.time.delay(10)

# Quit the game
pygame.quit()
