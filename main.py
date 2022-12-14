def on_overlap_tile(sprite, location):
    global Current_Level, enemy2
    Current_Level += 1
    Change_Level(Current_Level)
    mySprite.set_stay_in_screen(True)
    enemy2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 1 1 1 . . . . . . . 
                    . . . . 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 f 1 1 f 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 . 1 . 1 . . 1 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(enemy2,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 f 1 1 f 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . 1 1 1 1 1 1 1 . . . . . . 
                        . . 1 1 1 1 1 1 1 1 . . . . . . 
                        . . 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 f 1 1 1 f 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 . . 1 . . 1 . . 1 . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . 1 1 1 1 1 1 1 . . . . . . . 
                        . 1 1 1 1 1 1 1 1 . . . . . . . 
                        . 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 f 1 1 1 1 f 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 . . 1 . . 1 . . 1 . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . 1 1 1 1 1 1 1 . . . . . 
                        . . . 1 1 1 1 1 1 1 1 . . . . . 
                        . . . 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 f 1 1 1 f 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 . . 1 . . 1 . . 1 . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 f 1 1 f 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 . . 1 . . 1 . . 1 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 f 1 1 f 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 . . 1 . . 1 . . 1 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 f 1 1 1 f 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 . . 1 . . 1 . . 1 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 f 1 1 f 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 . . 1 . . 1 . . 1 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 1 1 1 1 1 1 1 . . 
                        . . . . . . 1 1 1 1 1 1 1 1 . . 
                        . . . . . . 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 f 1 1 1 f 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 . . 1 . . 1 . . 1 .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 f 1 1 1 f 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 f 1 1 f 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 f 1 1 1 f 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        500,
        True)
    enemy2.say_text("You can only have my chest if you defeat me", 5000, True)
    enemy2.follow(mySprite, 15)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . b . . . . . . . . . 
                    . . . e e e b b b b b b . . . . 
                    . . . e e e b b b b b b . . . . 
                    . . . . . . b . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        50,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    global Current_Level
    Current_Level += 1
    Change_Level(Current_Level)
    tiles.place_on_random_tile(mySprite, sprites.dungeon.floor_light2)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.door_open_east,
    on_overlap_tile2)

def on_on_zero(status):
    enemy2.destroy()
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def Change_Level(Level_Number: number):
    if Level_Number == 1:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
    elif Level_Number == 2:
        tiles.set_current_tilemap(tilemap("""
            level8
        """))
    elif Level_Number == 3:
        tiles.set_current_tilemap(tilemap("""
            level9
        """))
    elif Level_Number == 4:
        tiles.set_current_tilemap(tilemap("""
            level11
        """))
    tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_insignia)

def on_overlap_tile3(sprite3, location3):
    global Current_Level
    Current_Level += 1
    Change_Level(Current_Level)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_dark_grass3,
    on_overlap_tile3)

def on_life_zero():
    if True:
        game.over(False, effects.dissolve)
info.on_life_zero(on_life_zero)

def on_on_overlap(sprite4, otherSprite):
    global mySprite2
    CHEST: Sprite = None
    CHEST.destroy(effects.cool_radial, 500)
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . f 5 5 5 5 5 f . . . . . 
                    . . . . f 5 5 f 5 5 f . . . . . 
                    . . . . f 5 5 f 5 5 f . . . . . 
                    . . . . f 5 5 f 5 5 f . . . . . 
                    . . . . f 5 5 5 5 5 f . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite5, otherSprite2):
    sprite5.destroy()
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite2).value += -15
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite6, otherSprite3):
    global enemy2, statusbar2
    enemy2.destroy()
    info.change_life_by(-1)
    enemy2.set_stay_in_screen(True)
    enemy2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . 1 1 1 . . . . . . . 
                    . . . . 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 f 1 1 f 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 1 1 1 1 1 1 1 . . . . . 
                    . . . 1 . 1 . 1 . . 1 . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(enemy2,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 f 1 1 f 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . 1 1 1 1 1 1 1 . . . . . . 
                        . . 1 1 1 1 1 1 1 1 . . . . . . 
                        . . 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 f 1 1 1 f 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 1 1 1 1 1 1 1 1 1 . . . . . 
                        . 1 . . 1 . . 1 . . 1 . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . 1 1 1 1 1 1 1 . . . . . . . 
                        . 1 1 1 1 1 1 1 1 . . . . . . . 
                        . 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 f 1 1 1 1 f 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 1 1 1 1 1 1 1 1 1 . . . . . . 
                        1 . . 1 . . 1 . . 1 . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . 1 1 1 1 1 1 1 . . . . . 
                        . . . 1 1 1 1 1 1 1 1 . . . . . 
                        . . . 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 f 1 1 1 f 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 1 1 1 1 1 1 1 1 1 . . . . 
                        . . 1 . . 1 . . 1 . . 1 . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 f 1 1 f 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 . . 1 . . 1 . . 1 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 . . . 
                        . . . . . 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 f 1 1 f 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                        . . . . 1 . . 1 . . 1 . . 1 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 f 1 1 1 f 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 . . 1 . . 1 . . 1 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 . 
                        . . . . . . . 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 f 1 1 f 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 1 1 1 1 1 1 1 1 1 
                        . . . . . . 1 . . 1 . . 1 . . 1 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 1 1 1 1 1 1 1 . . 
                        . . . . . . 1 1 1 1 1 1 1 1 . . 
                        . . . . . . 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 f 1 1 1 f 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 1 1 1 1 1 1 1 1 1 . 
                        . . . . . 1 . . 1 . . 1 . . 1 .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 f 1 1 1 f 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 f 1 1 f 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 . . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 f 1 1 1 f 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 1 . . 1 . . 1 . . 1 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        500,
        True)
    enemy2.follow(mySprite, 15)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar2.attach_to_sprite(enemy2)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

statusbar2: StatusBarSprite = None
mySprite2: Sprite = None
projectile: Sprite = None
enemy2: Sprite = None
Current_Level = 0
mySprite: Sprite = None
scene.set_background_color(15)
controller.start_light_animation(light.sparkle_animation, 5000)
mySprite = sprites.create(assets.image("""
    girl
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.say_text("let's go on a quest ", 2000, True)
info.set_life(3)
scene.camera_follow_sprite(mySprite)
Change_Level(1)
myMinimap = minimap.minimap(MinimapScale.HALF, 2, 3)
minimap.include_sprite(myMinimap, mySprite)