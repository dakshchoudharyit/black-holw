import pygame
import math
import random

pygame.init()

# ---------------- WINDOW ----------------
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Simulation")

clock = pygame.time.Clock()

# ---------------- CONSTANTS ----------------
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

G = 2500                 # Gravity strength (simulation scale)
BLACK_HOLE_MASS = 500
EVENT_HORIZON = 35

MAX_TRAIL = 300

FONT = pygame.font.SysFont("Arial", 18)
BIG_FONT = pygame.font.SysFont("Arial", 28, bold=True)


# ---------------- STAR CLASS ----------------
class Star:
    def __init__(self, x, y, vx, vy, color=None):
        self.x = float(x)
        self.y = float(y)

        self.vx = float(vx)
        self.vy = float(vy)

        self.radius = random.randint(3, 6)

        self.color = color or random.choice([
            (255, 220, 80),
            (80, 180, 255),
            (255, 80, 80),
            (100, 255, 130),
            (210, 100, 255)
        ])

        self.trail = []
        self.alive = True

    def update(self):
        if not self.alive:
            return

        dx = CENTER_X - self.x
        dy = CENTER_Y - self.y

        dist_sq = dx * dx + dy * dy
        distance = math.sqrt(dist_sq)

        # Captured by black hole
        if distance < EVENT_HORIZON:
            self.alive = False
            return

        # Prevent extreme forces
        distance = max(distance, EVENT_HORIZON)

        # Newtonian gravity
        acceleration = G * BLACK_HOLE_MASS / (distance * distance)

        ax = acceleration * dx / distance
        ay = acceleration * dy / distance

        # Update velocity
        self.vx += ax * 0.01
        self.vy += ay * 0.01

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Save trail
        self.trail.append((self.x, self.y))

        if len(self.trail) > MAX_TRAIL:
            self.trail.pop(0)

    def draw(self, surface):
        if not self.alive:
            return

        # Draw trajectory
        if len(self.trail) > 1:
            pygame.draw.lines(
                surface,
                self.color,
                False,
                [(int(x), int(y)) for x, y in self.trail],
                1
            )

        # Glow
        pygame.draw.circle(
            surface,
            (*self.color, 60),
            (int(self.x), int(self.y)),
            self.radius * 3
        )

        # Star
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )


# ---------------- CREATE STARS ----------------
def create_stars():
    stars = []

    # Designed for different orbital behaviors
    stars.append(Star(850, 400, 0, 3.2))
    stars.append(Star(300, 300, 0, -2.8))
    stars.append(Star(700, 200, -2.8, 0))
    stars.append(Star(950, 600, -1.8, -1.0))
    stars.append(Star(500, 650, 2.5, 0))

    return stars


stars = create_stars()


# ---------------- DRAW BACKGROUND STARS ----------------
background_stars = []

for _ in range(300):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    brightness = random.randint(50, 180)
    size = random.choice([1, 1, 1, 2])

    background_stars.append((x, y, brightness, size))


def draw_background():
    screen.fill((2, 3, 8))

    for x, y, brightness, size in background_stars:
        pygame.draw.circle(
            screen,
            (brightness, brightness, brightness),
            (x, y),
            size
        )


# ---------------- BLACK HOLE ----------------
def draw_black_hole(time_value):

    # Accretion disk
    for r in range(180, 50, -4):

        intensity = int(
            80 + 100 * math.sin(time_value * 2 + r * 0.05)
        )

        intensity = max(20, min(255, intensity))

        color = (
            min(255, intensity + 100),
            min(180, intensity // 2),
            20
        )

        pygame.draw.ellipse(
            screen,
            color,
            (
                CENTER_X - r,
                CENTER_Y - r // 3,
                r * 2,
                max(10, r * 2 // 3)
            ),
            2
        )

    # Outer glow
    for r in range(EVENT_HORIZON + 35, EVENT_HORIZON, -3):
        alpha_strength = max(20, 200 - r * 3)

        color = (
            alpha_strength,
            alpha_strength // 3,
            0
        )

        pygame.draw.circle(
            screen,
            color,
            (CENTER_X, CENTER_Y),
            r,
            2
        )

    # Event horizon
    pygame.draw.circle(
        screen,
        (0, 0, 0),
        (CENTER_X, CENTER_Y),
        EVENT_HORIZON
    )

    # Border
    pygame.draw.circle(
        screen,
        (255, 140, 30),
        (CENTER_X, CENTER_Y),
        EVENT_HORIZON,
        2
    )


# ---------------- UI ----------------
def draw_ui(paused, captured):

    status = "PAUSED" if paused else "RUNNING"

    text = BIG_FONT.render(
        "BLACK HOLE SIMULATION",
        True,
        (220, 220, 255)
    )

    screen.blit(text, (20, 20))

    info = [
        f"Status: {status}",
        f"Stars Active: {len([s for s in stars if s.alive])}",
        f"Stars Captured: {captured}",
        f"Black Hole Mass: {BLACK_HOLE_MASS}",
        "",
        "Controls:",
        "SPACE = Pause",
        "R = Reset",
        "Mouse Click = Add Star",
        "Mouse Wheel = Change Black Hole Mass"
    ]

    y = 65

    for line in info:

        color = (180, 255, 180)

        if "Captured" in line:
            color = (255, 120, 120)

        text = FONT.render(line, True, color)

        screen.blit(text, (20, y))

        y += 25


# ---------------- MAIN LOOP ----------------
running = True
paused = False
captured = 0
time_value = 0

while running:

    dt = clock.tick(60) / 1000
    time_value += dt

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Pause
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                paused = not paused

            # Reset
            if event.key == pygame.K_r:
                stars = create_stars()
                captured = 0

        # Add star with mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mx, my = pygame.mouse.get_pos()

                # Velocity perpendicular to direction
                dx = mx - CENTER_X
                dy = my - CENTER_Y

                distance = math.sqrt(dx * dx + dy * dy)

                if distance > 0:

                    # Tangential velocity
                    speed = random.uniform(2, 4)

                    vx = -dy / distance * speed
                    vy = dx / distance * speed

                    stars.append(
                        Star(mx, my, vx, vy)
                    )

            # Mouse wheel changes mass
            elif event.button == 4:
                BLACK_HOLE_MASS += 50

            elif event.button == 5:
                BLACK_HOLE_MASS = max(
                    50,
                    BLACK_HOLE_MASS - 50
                )

    # ---------------- UPDATE ----------------
    if not paused:

        for star in stars:

            was_alive = star.alive

            star.update()

            if was_alive and not star.alive:
                captured += 1

    # ---------------- DRAW ----------------
    draw_background()

    draw_black_hole(time_value)

    for star in stars:
        star.draw(screen)

    draw_ui(paused, captured)

    pygame.display.flip()


pygame.quit()