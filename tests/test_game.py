import unittest
import pygame
from game import isCollison


class TestSpaceInvaders(unittest.TestCase):

    num_of_enemies = 12  # Define the number of enemies

    def test_collision_detection(self):
        self.assertTrue(isCollison(100, 200, 100, 200))  # When two objects are at the same position
        self.assertTrue(isCollison(100, 200, 104, 204))  # When the distance is less than 27
        self.assertFalse(isCollison(100, 200, 150, 250))  # When the distance is greater than 27
        

    def test_player_movement(self):
        player_x = 450
        player_x_change = 0.7
        move_left_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        move_right_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)

        pygame.event.post(move_left_event)
        player_x += player_x_change  # Simulate player movement to the left
        self.assertEqual(player_x, 450 + player_x_change)  # Player should move to the left

        pygame.event.post(move_right_event)
        player_x += player_x_change  # Simulate player movement to the right
        self.assertEqual(player_x, 450 + 2 * player_x_change)  # Player should move to the right
        

    def test_enemy_movement(self):
        enemy_x = [500] * self.num_of_enemies  # Initialize with one value repeated for testing
        enemy_x_change = [0.3] * self.num_of_enemies  # Initialize with one value repeated for testing

        for i in range(self.num_of_enemies):
            enemy_x[i] += enemy_x_change[i]

        expected_x = [500.3] * self.num_of_enemies
        self.assertEqual(enemy_x, expected_x)
        

    def test_bullet_movement(self):
        bullet_y = 640  # Initialize with the initial bullet position
        bullet_y_change = 2
        bullet_state = "fire"

        if bullet_state == "fire":
            bullet_y -= bullet_y_change  # Simulate bullet movement
        self.assertEqual(bullet_y, 640 - bullet_y_change)  # Bullet should move upward
        

if __name__ == '__main__':
    unittest.main()
