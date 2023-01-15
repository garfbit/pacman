hero = game.create_sprite(2, 2)
food = game.create_sprite(4, 4)
ghost = game.create_sprite(0, 0)
ghost.change(LedSpriteProperty.BLINK, 100)
ghost.set(LedSpriteProperty.BRIGHTNESS, 10)
food.set(LedSpriteProperty.BRIGHTNESS, 5)
while True:
    basic.pause(400)
    if ghost.get(LedSpriteProperty.X) < hero.get(LedSpriteProperty.X):
        ghost.change(LedSpriteProperty.X, 1)
    elif ghost.get(LedSpriteProperty.X) > hero.get(LedSpriteProperty.X):
        ghost.change(LedSpriteProperty.X, -1)
    elif ghost.get(LedSpriteProperty.Y) < hero.get(LedSpriteProperty.Y):
        ghost.change(LedSpriteProperty.Y, 1)
    elif ghost.get(LedSpriteProperty.Y) > hero.get(LedSpriteProperty.Y):
        ghost.change(LedSpriteProperty.Y, -1)
    if input.acceleration(Dimension.X) > 200:
        hero.change(LedSpriteProperty.X, 1)
    elif input.acceleration(Dimension.X) < -200:
        hero.change(LedSpriteProperty.X, -1)
    if input.acceleration(Dimension.Y) > 200:
        hero.change(LedSpriteProperty.Y, 1)
    elif input.acceleration(Dimension.Y) < -200:
        hero.change(LedSpriteProperty.Y, -1)
    if hero.is_touching(food):
        game.add_score(1)
        food.set(LedSpriteProperty.X, randint(0, 5))
        food.set(LedSpriteProperty.Y, randint(0, 5))
        if food.get(LedSpriteProperty.X) < 2 and food.get(LedSpriteProperty.Y) < 2:
            ghost.set(LedSpriteProperty.X, 4)
            ghost.set(LedSpriteProperty.Y, 4)
        elif food.get(LedSpriteProperty.X) > 2 and food.get(LedSpriteProperty.Y) < 2:
            ghost.set(LedSpriteProperty.X, 0)
            ghost.set(LedSpriteProperty.Y, 4)
        elif food.get(LedSpriteProperty.X) < 2 and food.get(LedSpriteProperty.Y) > 2:
            ghost.set(LedSpriteProperty.X, 4)
            ghost.set(LedSpriteProperty.Y, 0)
        else:
            ghost.set(LedSpriteProperty.X, 0)
            ghost.set(LedSpriteProperty.Y, 0)
    if hero.is_touching(ghost):
        game.game_over()
ghost.set(LedSpriteProperty.X, 4)