import tempfile
import unittest
from pathlib import Path

from local_connection import add_repository_item, connect_local_repository, list_repository_items


class LocalConnectionTests(unittest.TestCase):
    def test_can_connect_and_persist_items_in_local_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            db_file = Path(temp_dir) / "repo.db"
            connection = connect_local_repository(str(db_file))
            self.addCleanup(connection.close)

            add_repository_item(connection, "newonboarding")
            add_repository_item(connection, "newonboarding")

            self.assertEqual(list_repository_items(connection), ["newonboarding"])
            self.assertTrue(db_file.exists())


if __name__ == "__main__":
    unittest.main()

