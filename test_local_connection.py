import tempfile
import unittest
from pathlib import Path

from local_connection import add_repository_item, connect_local_repository, list_repository_items


class LocalConnectionTest(unittest.TestCase):
    def test_can_connect_and_persist_items_in_local_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            db_file = Path(temp_dir) / "repo.db"
            connection = connect_local_repository(str(db_file))
            self.addCleanup(connection.close)

            add_repository_item(connection, "newonboarding")
            add_repository_item(connection, "newonboarding")

            items = list_repository_items(connection)
            self.assertEqual(len(items), 1)
            self.assertEqual(items, ["newonboarding"])
            self.assertTrue(db_file.exists())

    def test_can_list_multiple_distinct_items(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            db_file = Path(temp_dir) / "repo.db"
            connection = connect_local_repository(str(db_file))
            self.addCleanup(connection.close)

            add_repository_item(connection, "repo-a")
            add_repository_item(connection, "repo-b")

            self.assertEqual(list_repository_items(connection), ["repo-a", "repo-b"])


if __name__ == "__main__":
    unittest.main()
