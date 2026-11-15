"""
PS 55 - Catch the Falling Objects
Language : Python 3        Library : Pygame

Run game  :  python catch_the_falling_objects.py
Run tests :  python catch_the_falling_objects.py test
"""
import random
import sys

#Constants
WIDTH, HEIGHT = 500, 600
BASKET_W, BASKET_H, BASKET_Y = 80, 20, 560
BASKET_SPEED = 10
OBJ_SIZE = 20
OBJ_SPEED = 5
START_LIVES = 3
FPS = 60


#Core logic (pure functions, testable)
def move_basket(basket_x, key_name):
    """Move basket 10 px on LEFT/RIGHT, keep it inside window. Other keys ignored."""
    if key_name == "LEFT":
        basket_x -= BASKET_SPEED
    elif key_name == "RIGHT":
        basket_x += BASKET_SPEED
    else:
        return basket_x  # invalid key -> ignored
    return max(0, min(WIDTH - BASKET_W, basket_x))


def is_caught(basket_x, obj_x, obj_y):
    """Rect collision between basket and object."""
    return (obj_x < basket_x + BASKET_W and obj_x + OBJ_SIZE > basket_x and
            obj_y < BASKET_Y + BASKET_H and obj_y + OBJ_SIZE > BASKET_Y)


def is_missed(obj_y):
    """Object has fallen past the bottom of the window."""
    return obj_y >= HEIGHT


def new_object_x():
    return random.randint(0, WIDTH - OBJ_SIZE)  # randint(0, 480)


def update_state(score, lives, basket_x, obj_x, obj_y):
    """
    Resolve one object. Returns (score, lives, status)
    status: 'caught' | 'missed' | 'game_over' | 'falling'
    """
    if is_caught(basket_x, obj_x, obj_y):
        return score + 1, lives, "caught"
    if is_missed(obj_y):
        lives -= 1
        return score, lives, ("game_over" if lives <= 0 else "missed")
    return score, lives, "falling"


#Test cases from the problem statement
def run_tests():
    # Test Case 1: normal input
    s, l, st = update_state(0, 3, 210, 230, 545)
    assert (st, s, l) == ("caught", 1, 3)
    print(f"TC1: Object caught | Score: {s} | Lives: {l}")

    # Test Case 2: boundary
    assert move_basket(0, "LEFT") == 0
    assert move_basket(420, "RIGHT") == 420
    print("TC2: (a) Basket x = 0 (no movement)  (b) Basket x = 420 (no movement)")

    # Test Case 3: invalid key
    assert move_basket(210, "UP") == 210
    print("TC3: Key ignored. Basket x = 210")

    # Test Case 4: different valid scenario
    s, l, st = update_state(0, 3, 210, 400, 600)
    assert (st, l) == ("missed", 2)
    print(f"TC4a: Object missed | Lives: {l}")
    s, l, st = update_state(7, 1, 210, 400, 600)
    assert (st, l, s) == ("game_over", 0, 7)
    print(f"TC4b: Object missed | Lives: {l} | Game Over | Final Score: {s}")
    print("All test cases passed.")


#Game
def main():
    import pygame

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Catch the Falling Objects")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 32)
    big_font = pygame.font.SysFont(None, 64)
    pygame.key.set_repeat(60, 30)  # hold key to keep moving

    def reset():
        return 0, START_LIVES, (WIDTH - BASKET_W) // 2, new_object_x(), 0

    score, lives, basket_x, obj_x, obj_y = reset()
    game_over = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:  # restart
                        score, lives, basket_x, obj_x, obj_y = reset()
                        game_over = False
                elif event.key == pygame.K_LEFT:
                    basket_x = move_basket(basket_x, "LEFT")
                elif event.key == pygame.K_RIGHT:
                    basket_x = move_basket(basket_x, "RIGHT")
                # any other key is ignored

        if not game_over:
            obj_y += OBJ_SPEED
            score, lives, status = update_state(score, lives, basket_x, obj_x, obj_y)
            if status in ("caught", "missed"):
                obj_x, obj_y = new_object_x(), 0
            elif status == "game_over":
                game_over = True

        # ---- Draw ----
        screen.fill((25, 25, 40))
        if not game_over:
            pygame.draw.rect(screen, (240, 200, 60), (obj_x, obj_y, OBJ_SIZE, OBJ_SIZE))
        pygame.draw.rect(screen, (80, 180, 255), (basket_x, BASKET_Y, BASKET_W, BASKET_H))
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"Lives: {max(lives, 0)}", True, (255, 255, 255)), (WIDTH - 110, 10))

        if game_over:
            over = big_font.render("Game Over", True, (255, 80, 80))
            final = font.render(f"Final Score: {score}", True, (255, 255, 255))
            hint = font.render("Press R to restart", True, (180, 180, 180))
            screen.blit(over, over.get_rect(center=(WIDTH // 2, 240)))
            screen.blit(final, final.get_rect(center=(WIDTH // 2, 300)))
            screen.blit(hint, hint.get_rect(center=(WIDTH // 2, 340)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()