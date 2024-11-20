import pygame
import sys
from linkFetch import getLinksByPrompt
from storeFetch import storeFetcher
from Convert import To_excel, To_json, To_csv_txt

# Initialize Pygame
pygame.init()

# Screen Dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BBScraping")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
button_width, button_height = 150, 50
excel_button = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 100), (button_width, button_height))
json_button = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 180), (button_width, button_height))
csv_button = pygame.Rect((SCREEN_WIDTH // 2 - button_width // 2, 260), (button_width, button_height))

# Table Parameters
ROW_HEIGHT = 80
COLUMN_WIDTH = 200
HEADER_HEIGHT = 50

TBFONT = pygame.font.Font("opens.ttf", 20)
TBHEADER_FONT = pygame.font.Font("opens.ttf", 30)

# Export Button
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
export_button = pygame.Rect(SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2, SCREEN_HEIGHT - 70, BUTTON_WIDTH, BUTTON_HEIGHT)

# Font Settings
TITLE_FONT = pygame.font.Font(None, 60)
FONT = pygame.font.Font(None, 40)

# Rectangles for Input Boxes
keyword_box = pygame.Rect(SCREEN_WIDTH // 2 - 300 // 2, 150, 300, 40)
area_box = pygame.Rect(SCREEN_WIDTH // 2 - 300 // 2, 230, 300, 40)

# Button Rect
button_box = pygame.Rect(SCREEN_WIDTH // 2 - 100 // 2, 320, 100, 50)

# Colors for Boxes
keyword_color = GRAY
area_color = GRAY

# Storage for Inputs
keyword = ''
area = ''
active_keyword = False
active_area = False

# Game Loop
clock = pygame.time.Clock()
running = True

# Loading screen
def loading_screen():
    screen.fill(WHITE)
    loading_text = FONT.render("Loading...", True, BLACK)
    screen.blit(loading_text, (SCREEN_WIDTH // 2 - loading_text.get_width() // 2,
                               SCREEN_HEIGHT // 2 - loading_text.get_height() // 2))
    pygame.display.flip()


while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle keyword input box
            if keyword_box.collidepoint(event.pos):
                active_keyword = True
                active_area = False
            # Toggle area input box
            elif area_box.collidepoint(event.pos):
                active_area = True
                active_keyword = False
            else:
                active_keyword = False
                active_area = False

            # Check if "Search" button is clicked
            if button_box.collidepoint(event.pos):
                loading_screen()
                pygame.event.get()
                searchArea = area
                searchKeyword = keyword

                storeLinks = getLinksByPrompt(searchArea, searchKeyword)
                storeData = storeFetcher(storeLinks, 10)
                print("Done fetching data")
                
                data=storeData
                scroll_offset = 0
                max_scroll = max(0, len(data) * ROW_HEIGHT - (SCREEN_HEIGHT - 100))

                # Render a single cell
                def render_cell(text, x, y, width, height, color=WHITE, border_color=BLACK):
                    pygame.draw.rect(screen, color, (x, y, width, height))
                    pygame.draw.rect(screen, border_color, (x, y, width, height), 1)
                    text_surface = TBFONT.render(text, True, BLACK)
                    screen.blit(
                        text_surface,
                        (x + 5, y + (height - text_surface.get_height()) // 2)
                    )



                # Main Loop
                clock = pygame.time.Clock()
                running = True

                while running:
                    screen.fill(WHITE)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        # Handle Scrolling
                        if event.type == pygame.MOUSEWHEEL:
                            scroll_offset -= event.y * 20
                            scroll_offset = max(0, min(scroll_offset, max_scroll))

                        # Handle Button Click
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if export_button.collidepoint(event.pos):
                                running =False
                                print("Exported clicked")

                    # Draw Header Row
                    headers = list(data[0].keys())
                    for col_idx, header in enumerate(headers):
                        render_cell(
                            header,
                            col_idx * COLUMN_WIDTH,
                            -scroll_offset,
                            COLUMN_WIDTH,
                            HEADER_HEIGHT,
                            color=GRAY
                        )

                    # Draw Data Rows
                    for row_idx, entry in enumerate(data):
                        for col_idx, key in enumerate(headers):
                            value = entry[key]
                            truncated_value = (value[:35] + '...') if len(value) > 35 else value
                            render_cell(
                                truncated_value,
                                col_idx * COLUMN_WIDTH,
                                HEADER_HEIGHT + row_idx * ROW_HEIGHT - scroll_offset,
                                COLUMN_WIDTH,
                                ROW_HEIGHT
                            )

                    # Draw Export Button
                    pygame.draw.rect(screen, GRAY, export_button)
                    button_text = TBFONT.render("Export", True, BLACK)
                    screen.blit(button_text, (export_button.x + BUTTON_WIDTH // 2 - button_text.get_width() // 2,
                                            export_button.y + BUTTON_HEIGHT // 2 - button_text.get_height() // 2))

                    pygame.display.flip()
                    clock.tick(30)
                
                
                clock = pygame.time.Clock()
                running = True

                while running:
                    screen.fill(WHITE)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if excel_button.collidepoint(event.pos):
                                To_excel(storeData  , name = "excel.xlsx" ,path = '')
                                running = False
                            elif json_button.collidepoint(event.pos):
                                To_json(storeData , "json.json" ,"")
                                running = False
                            elif csv_button.collidepoint(event.pos):
                                To_csv_txt(storeData , "csv.csv" , "")
                                running = False
                    # Draw Buttons
                    pygame.draw.rect(screen, GRAY, excel_button)
                    pygame.draw.rect(screen, GRAY, json_button)
                    pygame.draw.rect(screen, GRAY, csv_button)

                    # Draw Text on Buttons
                    excel_text = FONT.render("Excel", True, BLACK)
                    json_text = FONT.render("JSON", True, BLACK)
                    csv_text = FONT.render("CSV", True, BLACK)

                    screen.blit(excel_text, (excel_button.x + button_width // 2 - excel_text.get_width() // 2,
                                            excel_button.y + button_height // 2 - excel_text.get_height() // 2))
                    screen.blit(json_text, (json_button.x + button_width // 2 - json_text.get_width() // 2,
                                            json_button.y + button_height // 2 - json_text.get_height() // 2))
                    screen.blit(csv_text, (csv_button.x + button_width // 2 - csv_text.get_width() // 2,
                                        csv_button.y + button_height // 2 - csv_text.get_height() // 2))

                    # Draw Title
                    title_text = FONT.render("Choose Format", True, BLACK)
                    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 30))

                    pygame.display.flip()
                    clock.tick(30)

                


                running = False

            # Update colors based on active box
            keyword_color = BLUE if active_keyword else GRAY
            area_color = BLUE if active_area else GRAY

        # Handle Keyboard Input
        if event.type == pygame.KEYDOWN:
            if active_keyword:
                if event.key == pygame.K_RETURN:
                    active_keyword = False
                elif event.key == pygame.K_BACKSPACE:
                    keyword = keyword[:-1]
                else:
                    keyword += event.unicode
            elif active_area:
                if event.key == pygame.K_RETURN:
                    active_area = False
                elif event.key == pygame.K_BACKSPACE:
                    area = area[:-1]
                else:
                    area += event.unicode

    # Draw the title
    title_surface = TITLE_FONT.render("BBScraping", True, BLACK)
    screen.blit(title_surface, (SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 30))

    # Draw the Keyword input box
    pygame.draw.rect(screen, keyword_color, keyword_box, 2)
    keyword_surface = FONT.render(keyword, True, BLACK)
    screen.blit(keyword_surface, (keyword_box.x + 5, keyword_box.y + 5))

    # Draw the Area input box
    pygame.draw.rect(screen, area_color, area_box, 2)
    area_surface = FONT.render(area, True, BLACK)
    screen.blit(area_surface, (area_box.x + 5, area_box.y + 5))

    # Draw field labels
    keyword_label = FONT.render("Keyword", True, BLACK)
    area_label = FONT.render("Area", True, BLACK)
    screen.blit(keyword_label, (keyword_box.x + keyword_box.width // 2 - keyword_label.get_width() // 2, 120))
    screen.blit(area_label, (area_box.x + area_box.width // 2 - area_label.get_width() // 2, 200))

    # Draw the Search button
    pygame.draw.rect(screen, GRAY, button_box)
    button_text = FONT.render("Search", True, BLACK)
    screen.blit(button_text, (button_box.x + button_box.width // 2 - button_text.get_width() // 2,
                              button_box.y + button_box.height // 2 - button_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
