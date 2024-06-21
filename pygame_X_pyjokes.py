import pygame
import pyjokes

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pyjokes in Pygame")

# Set up font
font = pygame.font.Font(None, 36)
line_height = font.get_linesize()

# Function to wrap text into multiple lines
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = words[0]
    for word in words[1:]:
        test_line = current_line + ' ' + word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

# Function to get and render a joke
def get_new_joke():
    joke = pyjokes.get_joke()
    wrapped_lines = wrap_text(joke, font, width - 40)  # Wrap text to fit within the window
    return wrapped_lines

# Function to create a button
def create_button(text, position, size):
    button_surface = pygame.Surface(size)
    button_surface.fill((0, 128, 255))
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(size[0]/2, size[1]/2))
    button_surface.blit(text_surface, text_rect)
    button_rect = button_surface.get_rect(center=position)
    return button_surface, button_rect

# Get the initial joke
wrapped_lines = get_new_joke()

# Create the "New Joke" button
button_text = "New Joke"
button_size = (200, 50)
button_position = (width/2, height - 50)
button_surface, button_rect = create_button(button_text, button_position, button_size)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                wrapped_lines = get_new_joke()

    # Fill the background with black
    window.fill((0, 0, 0))

    # Draw the joke text
    y_offset = (height / 2) - (len(wrapped_lines) * line_height / 2)
    for line in wrapped_lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width/2, y_offset))
        window.blit(text_surface, text_rect)
        y_offset += line_height

    # Draw the button
    window.blit(button_surface, button_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
