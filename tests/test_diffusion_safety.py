import unittest

from diffusion_safety import adaptive_lambda, pareto_frontier


class DiffusionSafetyTests(unittest.TestCase):
    def test_adaptive_lambda_is_zero_outside_window(self):
        self.assertEqual(adaptive_lambda(80, 0.3, 0.2, timestep=5), 0.0)
        self.assertEqual(adaptive_lambda(80, 0.3, 0.2, timestep=45), 0.0)

    def test_adaptive_lambda_increases_with_violation_margin(self):
        low = adaptive_lambda(80, 0.19, 0.2, timestep=25)
        high = adaptive_lambda(80, 0.30, 0.2, timestep=25)
        self.assertLess(low, high)

    def test_pareto_frontier_removes_dominated_rows(self):
        rows = [
            {"method": "vanilla", "unsafe": 0.097, "align": 0.256},
            {"method": "dominated", "unsafe": 0.120, "align": 0.200},
            {"method": "strict", "unsafe": 0.027, "align": 0.206},
        ]
        frontier = pareto_frontier(rows, minimize=("unsafe",), maximize=("align",))
        methods = {row["method"] for row in frontier}
        self.assertNotIn("dominated", methods)
        self.assertIn("vanilla", methods)
        self.assertIn("strict", methods)


if __name__ == "__main__":
    unittest.main()
