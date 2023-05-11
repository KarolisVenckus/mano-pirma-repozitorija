import unittest
from game import Character, Enemy, Game


class TestCharacter(unittest.TestCase):
    def test_attack(self):
        c1 = Character("Player", 100, 10, 5)
        c2 = Character("Enemy", 50, 5, 2)

        c1.attack(c2)
        self.assertEqual(c2.health, 45)

        c2.attack(c1)
        self.assertEqual(c1.health, 95)

    def test_defend(self):
        c1 = Character("Player", 100, 10, 5)

        c1.defend()
        self.assertEqual(c1.defense_power, 7)


class TestEnemy(unittest.TestCase):
    def test_reward(self):
        e1 = Enemy("Goblin", 50, 5, 2, 10)
        self.assertEqual(e1.reward, 10)

        e2 = Enemy("Dragon", 200, 20, 10, 50)
        self.assertEqual(e2.reward, 50)


class TestGame(unittest.TestCase):
    def test_game(self):
        game = Game("Test Player")

        # Test that player starts with full health
        self.assertEqual(game.player.health, 100)

        # Test that player can defeat enemy and gain reward
        enemy = game.enemies[0]
        game.player.attack(enemy)
        self.assertFalse(enemy.is_alive())
        self.assertEqual(game.player.health, 100)
        self.assertEqual(game.player.defense_power, 0)
        self.assertEqual(game.player.reward, 10)

        # Test that player can defend and gain defense power
        game.player.reset()
        game.player.defend()
        self.assertEqual(game.player.defense_power, 7)

        # Test that player can die and game ends
        game.player.reset()
        game.player.health = 1
        with self.assertRaises(SystemExit):
            game.run()


if __name__ == '__main__':
    unittest.main()