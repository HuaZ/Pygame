class Settings():

    def __init__(self):

        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship sittings
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien sittings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        self.fleet_direction = 1
